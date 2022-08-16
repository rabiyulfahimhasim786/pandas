import pandas as pd
d1 = {'col1': [1, 2, 3 ,4], 'col2': ['a','x','e', 'f'], 'col3':['q','w','y','v'], 'col2': ['a','x',3, 'f'], }

df = pd.DataFrame(data=d1)
#display(df)
df.to_csv('demo.csv')