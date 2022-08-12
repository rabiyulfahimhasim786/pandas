
import pandas as pd
df = pd.read_excel('orderquoteline.xlsx', sheet_name=None)
df['Sheet1'].to_csv('orderquoteline1.csv') 