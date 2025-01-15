import pandas as pd

data1 = {"Emp Id": ["e1","e2","e3","e4","e5"],
         "Names" : ["R", "S","A","E","P"],
         "Age" : [34,54,23,54,43]}

data2 = {"Emp Id": ["e1","e2","e3","e4","e5"],
         "Salary":[45000,34000,34400,50000,60000]}

df1= pd.DataFrame(data1)
df2=pd.DataFrame(data2)
# print(df1)
# print(df2)

print(pd.merge(df1,df2,on="Emp Id"))