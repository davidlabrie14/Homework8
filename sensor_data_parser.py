import os
import time
import sys 
import csv 
  
# csv file name 
filename = "raw_data.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 

for row in rows[:int(csvreader.line_num)]: 

    for col in row: 
        print("%10s"%col), 
    print('\n') 

