import pandas as pd

#using goodbye func

data = pd.read_excel("ESD.xlsx")
# print(data)
# gp = data.groupby("Department").agg({"Gender":"count"})
# print(gp) #returns count of department count
# gp1= data.groupby(["Department", "Gender"]).agg({"EEID":"count"})
# print(gp1)

gp2 = data.groupby("Country").agg({"Age":"mean"})
print(gp2)

gp3 = data.groupby(["Country", "Gender"]).agg({"Annual Salary": "max"})
print(gp3)