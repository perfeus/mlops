# Module 1

This project demonstrates an example of creating a simple pipeline using Python. The process involves several stages such as data creation, preprocessing, model training, and testing.

## Stages of the Process:

### 1. Data Creation (data_creation.py)
The Python script `data_creation.py` creates various time series datasets describing a random process. The datasets may contain anomalies or noise. Part of the datasets is saved in the `train` folder, and the other part is saved in the `test` folder.

### 2. Data Preprocessing (model_preprocessing.py)
The Python script `model_preprocessing.py` preprocesses the data using `sklearn.preprocessing.StandardScaler`. This stage prepares the data for model training. [Find more details using the link](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

### 3. Model Preparation and Training (model_preparation.py)
The Python script `model_preparation.py` creates and trains a Linear Regression model on the data prepared in the previous stage. [Find more details using the link](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression)

### 4. Model Testing (model_testing.py)
The Python script `model_testing.py` evaluates the machine learning model on the data from the `test` folder. This stage allows assessing the model's performance on new data. `r2_score` has been taken as a key metric. [Find more details using the link](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score)

## Running the Process:

To run the entire process automatically, you can use the bash script `pipeline.sh`, which sequentially executes all Python scripts. Run the script with the following command:

```bash
./pipeline.sh 1000 3 2 0
```

In the example you'll get dataset with 1000 rows, linear model with polynomial degree equals 3, noise distributed normaly with stadard deviation 2 and number of anomalies in the dataset is 0. 

## Environment Requirements:
To successfully execute the process, you need Python and the libraries listed in the requirements.txt file installed. You can install them by running the following command:

```bash
pip install -r requirements.txt
```

# Module 2

This project aims to streamline the machine learning workflow using Jenkins pipelines. The pipeline automates the process of creating datasets, preprocessing data, training models, and testing models. The entire workflow is orchestrated using Jenkins, ensuring consistency and reproducibility across different stages of the machine learning pipeline.

## Pipeline Stages:

### 1. Environment Info
Display information about the environment, including the current working directory and the location of the Python 3 interpreter.
### 2. Create Dataset
Execute the data_creation.py script to generate datasets required for training and testing models.
### 3. Preprocess Dataset
Run the model_preprocessing.py script to preprocess the generated datasets before training the model.
### 4. Train Model
Execute the model_preparation.py script to train machine learning models using the preprocessed datasets.
### 5. Test Model
Run the model_testing.py script to evaluate the performance of trained models on test datasets.

## Usage:

### 1. Build docker image
To build a docker image use Dockerfile and run the command:
```bash
docker build -t myimage:v01 .
```
### 2. Run docker container
To run docker container user the command:
```bash
docker run -d --name jenkins -p 88:8080 -p 50000:50000 myimage:v01
```
### 3. Configuration
Configure the pipeline according to your project requirements, such as adjusting paths to scripts.
### 4. Monitoring
Trigger the pipeline execution, either manually or automatically based on configured triggers.
Monitor the pipeline execution in the Jenkins dashboard to track progress and view logs.

## Post-Build Actions:
The pipeline includes a post-build action to echo "Pipeline has completed!" This step runs after each pipeline execution, providing feedback that the pipeline has finished.

# Module 3

Web Server: This service, named web-server, is designed to run a web application using the image [sndbox44/titanic:latest](https://hub.docker.com/repository/docker/sndbox44/titanic/general) from Docker Hub. It exposes port 5000 on the host machine and forwards traffic to port 5000 within the container. The container is named 'app' and is configured to restart unless explicitly stopped.
Continuous Integration: The continues-integration service is responsible for running Jenkins using the image [sndbox44/jenkinspy:latest](https://hub.docker.com/repository/docker/sndbox44/jenkinspy/general) from Docker Hub. It exposes ports 88 and 50000 on the host machine for accessing Jenkins' web interface and handling Jenkins agent communication, respectively. The container is named 'jen' and is also set to restart unless explicitly stopped.

## Setup Instructions:
1. Ensure Docker is installed on your machine.
2. Clone this repository.
3. Navigate to the project directory.
Run docker-compose up to start the services:
```bash
docker compose up -d
```

## Usage:
1. Access the web application by visiting http://localhost:5000 in your web browser.
2. Access Jenkins' web interface by visiting http://localhost:88.
3. Set up Jenkins jobs and pipelines as needed for continuous integration and deployment.

# Mudule 4

The project is aimed to demonstrate skills in using the DVC (data version control) utility. In the project Google Drive is used as dvc remote repository [link](https://drive.google.com/drive/folders/1Vre7BSCadkYkooFwCZMxEAHccx1js0Ch?usp=drive_link) and data imported from catboost.datasets module:
```bash
from catboost.datasets import titanic
train, test = titanic()
```

## Steps:
1. Create a dataset with create_datasets.py.
2. Modify the dataset with modify_datasets.py.
3. Impute nan values in the 'Age' column with its mean.
4. Apply one-hot-encoding to 'Sex' column.

## Conclusion:
Upon successful completion of the all steps, a Git repository with published metadata and a folder on Google Drive containing different versions of the datasets will be created.

# Mudule 5

The project is aimed to demonstrate the process of testing dataset with the help of Pytest library. In the project Google Drive is used as dvc remote repository [link](https://drive.google.com/drive/folders/1Vre7BSCadkYkooFwCZMxEAHccx1js0Ch?usp=drive_link) and data imported from Kaggle [link](https://www.kaggle.com/datasets/mirichoi0218/insurance). CI and testing processes are carried out with the help of docker image [link](https://hub.docker.com/repository/docker/sndbox44/jenkins/general) and to run container follow the next command as an example:

```bash
docker run -d --rm --name jen -v jenkins:/var/jenkins_home/data -p 80:8080 -p 50000:50000 jenkins:latest
```
Before the commnad above create volume 'jenkins' on a local machine and place there kaggle.json file with your credentals to access the data on Kaggle


## Pipeline Stages
The pipeline consists of the following stages:

### 1. Environment Info
- Displays the current environment information.
- Prints the system PATH.
- Shows the current working directory.
- Locates the Python 3 binary.
- Copies the kaggle.json credentials file to the appropriate directory.
- Copy Credentials
Ensures that the kaggle.json credentials file is copied to the workspace directory required for the dataset creation.

### 2. Create Dataset
- Executes the Jupyter Notebook (lab5.ipynb) to generate the dataset.
- Converts the notebook to a Python script for execution.

### 3. Test Dataset
- Verifies the integrity and correctness of the dataset by running predefined tests using pytest.

### 4. Post Actions
- Always Run
- Executes a final step to notify that the pipeline has completed, regardless of the outcome of the previous stages.

## Prerequisites
- Jenkins: Ensure you have Jenkins installed and running.
- Docker Pipeline Plugin: This plugin must be installed in Jenkins to facilitate the pipeline execution.
- Jupyter: Jupyter must be installed and accessible in the environment where the pipeline runs.
- Python: Python 3 must be installed and available in the system PATH.

## Usage
- Clone the repository to your local machine or directly to the Jenkins server.
- Ensure the kaggle.json file is available at /var/jenkins_home/data/kaggle.json.
- Set up the Jenkins job to use the Jenkinsfile provided in this repository.
- Run the pipeline job from the Jenkins interface.

## Troubleshooting
- Ensure that all necessary dependencies (Jupyter, Python, pytest) are installed and correctly configured.
- Verify that the kaggle.json file has the correct permissions and is accessible by the Jenkins user.
- Check the Jenkins job logs for any error messages and resolve them accordingly.
