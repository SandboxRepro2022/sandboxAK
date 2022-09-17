import pandas as pd
df=pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/dc7663c7-5da9-4765-a98b-ba4bc9de9079",delimiter=";")
df.groupby
df=df.groupby("Semaine").sum()
df2=df.copy()
df2=df2.reset_index()
print(df2)
df2=df2[["Semaine","NewAdmHospit"]]
df2.to_csv("groupby.csv",sep=";",index=False)