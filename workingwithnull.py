import pandas as pd

data =  pd.read_csv("company1.csv")

print(data)
# print(data.isnull())
# print(data.isnull().sum())

print(data.dropna())