import numpy as np  # to work with arrays
# to standardize the data
from sklearn.preprocessing import StandardScaler


# load the train data
data = np.genfromtxt('./train/data.csv', delimiter=',')
# train the standard scaler
scaler = StandardScaler()
# standardize the train data
data[:, 0] = scaler.fit_transform(data[:, 0].reshape(-1, 1)).reshape(-1)
# save the train data
np.savetxt('./train/data.csv', data, delimiter=',', fmt='%f')
# load the test data
data = np.genfromtxt('./test/data.csv', delimiter=',')
# standardize the test data
data[:, 0] = scaler.transform(data[:, 0].reshape(-1, 1)).reshape(-1)
# save the test data
np.savetxt('./test/data.csv', data, delimiter=',', fmt='%f')
