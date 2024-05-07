import pandas as pd

# Load the dataset
data = pd.read_csv('datasets/titanic.csv')
# One-hot encode
data['Sex'] = data.loc[:, 'Sex'].apply(lambda x: 1 if x == 'male' else 0)
# Save modified dataset
data.to_csv('datasets/titanic.csv', index=False)
