import csv

bottle_list = []

# Read all data from the csv file.
with open('test.csv', 'rb') as b:
    bottles = csv.reader(b)
    bottle_list.extend(bottles)

# data to override in the format {line_num_to_override:data_to_write}. 
line_to_override = {5:['3', '2', '1'] }

# Write data to the csv file and replace the lines in the line_to_override dict.
with open('test.csv', 'wb') as b:
    writer = csv.writer(b)
    for line, row in enumerate(bottle_list):
         data = line_to_override.get(line, row)
         writer.writerow(data)
