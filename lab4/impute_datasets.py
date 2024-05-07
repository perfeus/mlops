import pandas as pd

# Load the dataset
data = pd.read_csv('datasets/titanic.csv')
# Impute missing values in the 'Age' column with the mean
data['Age'] = data['Age'].fillna(data['Age'].mean())
# Save modified dataset
data.to_csv('datasets/titanic.csv', index=False)