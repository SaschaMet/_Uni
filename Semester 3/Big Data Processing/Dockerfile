# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of these directories to the working directory in the container
COPY . .

CMD ['python', 'pipeline/run_pipeline.py']
CMD ['python', '-m', 'model.model.py']
CMD ['chmod' + 'u+x' + 'save_model_to_S3.sh']
CMD ['save_model_to_S3.sh']