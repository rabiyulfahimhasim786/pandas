import pandas as pd 

df = pd.read_csv('Alldetails.csv')
#print(df.head())
#newdf = df[row[0]>1]]
newdf = df.iloc[:,4]
print(newdf)
