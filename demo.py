

import pandas as pd

data = {"Name": ["John","Peter","Lisa"],
        "Age": [25,24,23],
        "Salary":[35000,25000,20000]}

df=pd.DataFrame(data)
print(df)


#for calling excel files

#data = pd.read_excel("filename_xlsx")
#print(data)
#print(data.info()) --> prints info detail about each row and thier description

