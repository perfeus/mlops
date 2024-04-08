import numpy as np  # to work with arrays
import os  # to work with directories and files
# to create polynomial features
from sklearn.preprocessing import PolynomialFeatures
# to create a linear regression model
from sklearn.linear_model import LinearRegression
# to create a pipelines
from sklearn.pipeline import Pipeline
# to split the data into training and testing sets
from sklearn.model_selection import train_test_split


# create constant values for the data size,
# polynomial degree, noise, and number of anomalies
data_size, poly_degree, noise, anomalies = 500, 4, 3, 0
# generate random data
x_data = np.arange(1, data_size + 1).reshape(-1, 1)
y = np.random.uniform(0, 200, (data_size, ))
# create model
model = Pipeline([('poly', PolynomialFeatures(degree=poly_degree)),
                  ('linear', LinearRegression())])
# fit the model
model.fit(x_data, y)
# add noise to predictions
y_data = model.predict(x_data) + np.random.normal(0, noise, (data_size, ))
# add anomalies
id_anomalies = np.random.choice(range(data_size), anomalies, replace=False)
y_data[id_anomalies] += np.random.uniform(-100, 100, anomalies)
# create dataset
data = np.concatenate((x_data, y_data.reshape(-1, 1)), axis=1)
# split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2)
# create the directories for train and test data
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)
# save the train and test data
np.savetxt('train/data.csv', train_data, delimiter=',', fmt='%f')
np.savetxt('test/data.csv', test_data, delimiter=',', fmt='%f')
