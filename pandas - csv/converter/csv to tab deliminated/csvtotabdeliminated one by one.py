#!/usr/bin/env python
import csv
import os
file='./demo'
with open(file+'.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            #csv_reader.next()  ## skip one line (the first one)
            newfile = file + '.txt'

            for line in csv_reader:
                with open(newfile, 'a') as new_txt:    #new file has .txt extn
                    txt_writer = csv.writer(new_txt, delimiter = '\t') #writefile
                    txt_writer.writerow(line)   #write the lines to file`