import pandas as pd

data = pd.read_csv("Titanic-Dataset_2.csv")
# print(data)

print(data.info())
print(data.head(10))
print(data.tail(10))
print(data.describe())





