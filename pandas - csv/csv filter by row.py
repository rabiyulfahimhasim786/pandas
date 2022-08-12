import pandas as pd 

df = pd.read_csv('test.csv')
#print(df.head())
newdf = df[df['E']>0]
print(newdf)
