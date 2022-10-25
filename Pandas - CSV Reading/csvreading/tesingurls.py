import json
import requests

r = requests.get('https://ocr.mobilteam.repl.co/texturl/')

print(r.json())
#print(r['data'])
#json_url = urlopen(url)

data = r.json()

print(data['data'][0]['key'])

import pandas as pd
#url = 'http://winterolympicsmedals.com/medals.csv'
#url = data['data'][0]['key']
url = 'https://tesxtractkvtable-us-east-1-660866612853.s3.amazonaws.com/tables/784af37594a19835c1a636e03b8bae1290a31c0abdcb6ea509c83f0da26290df/table_e919d1fbf71343c7a52f7ed18b4bcb5a_page_1.csv'
df = pd.read_csv(url)   
df.head()
df.to_csv('table.csv', index=False)