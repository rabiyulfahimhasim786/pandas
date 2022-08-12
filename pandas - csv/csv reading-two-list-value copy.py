
import pandas as pd
import csv
with open('Alldetails.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    fsa=[]
    a = []
    for row in reader:
        count = count+1
        #print(row[2])
        fsa.append(row[0])
        a.append(row[1])
print(fsa[0:])
print(a[4:])