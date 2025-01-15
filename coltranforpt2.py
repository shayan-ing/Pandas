import pandas as pd

# data = pd.read_csv("company.csv")

# print(data)

# data["Bonus"] = (data["salary"]/100)*20
# print(data)

data = {"Months": ["January","February","March","April"]}
a = pd.DataFrame(data)
print(a)

def extract(value):
    return value[0:3]

a["Short_Months"] = a["Months"].map(extract)
print(a)