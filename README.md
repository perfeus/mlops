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
