import pandas as pd

# Load the dataset
data = pd.read_csv('datasets/titanic.csv')
# Save modified dataset
data[['Pclass', 'Sex', 'Age']].to_csv('datasets/titanic.csv', index=False)
