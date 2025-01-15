import pandas as pd

data = pd.read_csv("company1.csv")
print(data)

# print(data["EEID"].duplicated()) #returns duplicate found in bool 
# print(data["EEID"].duplicated().sum()) #gives sum of duplicates found
# print(data.drop_duplicates("EEID")) #removes duplicate  always go for unique key