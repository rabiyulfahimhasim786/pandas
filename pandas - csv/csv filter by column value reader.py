
import pandas as pd
import csv
with open('testing.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    fsa=[]
    line = []
    desc = []
    Itemid = []
    UOM = []
    qty = []
    for row in reader:
        count = count+1
        #print(row[2])
        fsa.append(row[0])
        line.append(row[1])
        desc.append(row[3])
        Itemid.append(row[4])
        UOM.append(row[6])
        qty.append(row[8])
print(fsa[0:])
print(line[4:])
print(desc[4:])
print(Itemid[4:])
print(UOM[4:])
print(qty[4:])