# Practice for MLOps

This project demonstrates an example of creating a simple pipeline using Python. The process involves several stages such as data creation, preprocessing, model training, and testing.

## Stages of the Process:

### 1. Data Creation (data_creation.py)
The Python script `data_creation.py` creates various datasets describing a certain process (e.g., daily temperature changes). The datasets may contain anomalies or noise. Part of the datasets is saved in the `train` folder, and the other part is saved in the `test` folder.

### 2. Data Preprocessing (model_preprocessing.py)
The Python script `model_preprocessing.py` preprocesses the data using `sklearn.preprocessing.StandardScaler` or other preprocessing methods as needed. This stage prepares the data for model training.

### 3. Model Preparation and Training (model_preparation.py)
The Python script `model_preparation.py` creates and trains a machine learning model on the data prepared in the previous stage. Any approach to model training, such as supervised or unsupervised learning, can be used here.

### 4. Model Testing (model_testing.py)
The Python script `model_testing.py` evaluates the machine learning model on the data from the `test` folder. This stage allows assessing the model's performance on new data.

## Running the Process:

To run the entire process automatically, you can use the bash script `pipeline.sh`, which sequentially executes all Python scripts. Run the script with the following command:

```bash
./pipeline.sh

