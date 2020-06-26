import dill
import pandas as pd
from flask import Flask, render_template, request, jsonify

# Define Flask web service
app = Flask(__name__)

# workaround since ClassType is missing
dill._dill._reverse_typemap['ClassType'] = type

# import the models
input_file = "../mlm_dumps/lr_model.pk"
with open(input_file, "rb") as input_file:
    lr_model = dill.load(input_file)

input_file = "../mlm_dumps/lasso_model.pk"
with open(input_file, "rb") as input_file:
    lasso_model = dill.load(input_file)

def createPrediction(data):
    inputValues = []
    columns = []
    for dic in data:
        for key in dic:
            inputValues.append(dic[key])
            columns.append(key)

    data = pd.DataFrame([inputValues], columns=columns)

    lr_prediction = lr_model.predict(data)
    lasso_prediction = lasso_model.predict(data)

    res = {
        "linear": lr_prediction.tolist()[0][0],
        "lasso": lasso_prediction.tolist()[0],
    }

    return res



# routes
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        jsonData = request.json
        prediction = createPrediction(jsonData)
        return jsonify(prediction)
    return {
        "msg": "Invalid"
    }

# Run app if directly called
if __name__ == "__main__":
    app.run(host='localhost', port=666, debug=True)
