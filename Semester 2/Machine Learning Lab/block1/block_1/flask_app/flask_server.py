
"""This skript deploys a simple flask Web server which serves a serialized MLM
:author: Michael Kohlegger
:date: 
"""


import pandas as pd
from flask import Flask, request, render_template, jsonify
import dill
from numpy import array
import datetime as dt

# workaround since ClassType is missing 
dill._dill._reverse_typemap['ClassType'] = type

input_file = "../mlm_dumps/lr_model.pk"
with open(input_file, "rb") as input_file:
    regressor = dill.load(input_file)

input_file = "../mlm_dumps/X_pipeline.pk"
with open(input_file, "rb") as input_file:
    X_pipeline = dill.load(input_file)

input_file = "../mlm_dumps/y_pipeline.pk"
with open(input_file, "rb") as input_file:
    y_pipeline = dill.load(input_file)


def create_prediction(
    longitude,
    latitude,
    housing_median_age,
    total_rooms,
    total_bedrooms,
    population,
    households,
    median_income,
    ocean_proximity
):
    """This method creates a prediction using a serialized machine learning model

    :param longitude: A measure of how far west a house is; a higher value is farther west
    :param latitude: A measure of how far north a house is; a higher value is farther north
    :param housing_median_age: Median age of a house within a block; a lower number is a newer building
    :param total_rooms: Total number of rooms within a block
    :param total_bedrooms: Total number of bedrooms within a block
    :param population: Total number of people residing within a block
    :param households: Total number of households, a group of people residing within a home unit, for a block
    :param median_income: Median income for households within a block of houses (measured in tens of thousands of US Dollars)
    :param dist_lt_1h_ocean: Distance measure; 1 if < 1h to the ocean.
    :param dist_inland: Distance measure; 1 if inland.
    :param dist_island: Distance measure; 1 if island.
    :param dist_near_bay: Distance measure; 1 if near bay.
    :param dist_near_ocean: Distance measure; 1 if near ocean.
    :return: Prediction as Float.
    """

    # Create data object
    data = [[
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        ocean_proximity
    ]]


    columns=[
        'longitude', 
        'latitude', 
        'housing_median_age', 
        'total_rooms', 
        'total_bedrooms', 
        'population', 
        'households', 
        'median_income', 
        'ocean_proximity'
    ]
    
    data = pd.DataFrame(data, columns=columns)
    print(data)

    # Scale data object
    scaled_data = X_pipeline.transform(data)

    # Generate prediction
    # Inverse scale prediction to original
    prediction = y_pipeline.inverse_transform(
        regressor.predict(scaled_data).reshape(-1,1)
    )[0][0]

    return prediction


# Define Flask web service
app = Flask(__name__)


# Display a short message when root is called
@app.route('/')
def home_call():
    return "This is a flask Web service."


@app.route('/predict', methods=['GET'])
def predict():
    """This method creates a prediction from a http request
    :
    """
    # Read request argurments with default = 0
    longitude = float(request.args.get('longitude', '0'))
    latitude = float(request.args.get('latitude', '0'))
    housing_median_age = float(request.args.get('housing_median_age', '0'))
    total_rooms = float(request.args.get('total_rooms', '0'))
    total_bedrooms = float(request.args.get('total_bedrooms', '0'))
    population = float(request.args.get('population', '0'))
    households = float(request.args.get('households', '0'))
    median_income = float(request.args.get('median_income', '0'))
    ocean_proximity = str(request.args.get('ocean_proximity', 'NEAR BAY'))

    # Create a new prediction for the incoming data
    prediction = create_prediction(
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        ocean_proximity
    )

    output_dictionary = {
        "utc_call_time": dt.datetime.utcnow(),
        "value_output": prediction,
        "message": "You can expect a median house value of " + str(prediction) + ".",
        "value_input": {
            "longitude": longitude, 
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "ocean_proximity": ocean_proximity
        }        
    }
    
    return jsonify(output_dictionary)


@app.route('/predict/form')
def form():
    return render_template("input.html", title="Medium House Value")


# Run app if directly called
if __name__ == "__main__":
    app.run(host='localhost', port=666, debug=False)
