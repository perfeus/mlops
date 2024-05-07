from catboost.datasets import titanic

# Load the Titanic dataset
train, _ = titanic()
train.to_csv('datasets/titanic.csv', index=False)
