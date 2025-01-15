import pandas as pd

df = pd.read_excel("ESD.xlsx")

# print(df)

df.loc[(df["Bonus %"]==0), "GetsBonus"] = "no bonus"
df.loc[(df["Bonus %"]> 0), "GetsBonus"] = "bonus"
print(df.head(10))
