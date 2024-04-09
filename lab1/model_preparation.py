import numpy as np  # to work with arrays
import sys  # to work with command line arguments
import joblib  # to save the model
# to create polynomial features
from sklearn.preprocessing import PolynomialFeatures
# to create a pipeline
from sklearn.pipeline import Pipeline
# to create linear regression model
from sklearn.linear_model import LinearRegression

# to get the polynomial degree
poly_degree = int(sys.argv[1])
# get the features and target
data = np.genfromtxt('./train/data.csv', delimiter=',')
x_train, y_train = data[:, 0].reshape(-1, 1), data[:, 1]
# create a pipeline
model = Pipeline([('poly', PolynomialFeatures(degree=poly_degree)),
                  ('linear', LinearRegression(fit_intercept=False))])
# fit the model
model.fit(x_train, y_train)
# save the model
joblib.dump(model, './model.pkl')
