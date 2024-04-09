import numpy as np  # to work with arrays
import joblib  # to load the model
# to load metric
from sklearn.metrics import r2_score


# load the model
model = joblib.load('./model.pkl')
# load the test data
data = np.genfromtxt('./test/data.csv', delimiter=',')
# evaluate the model
print(r2_score(data[:, 1], model.predict(data[:, 0].reshape(-1, 1))))
