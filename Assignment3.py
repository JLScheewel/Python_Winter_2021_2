import os

from urllib.request import urlopen

csv = ['GOOG.csv', 'IBM.csv', 'MSFT.csv']
csv_modified = ['GOOG_modified.csv', 'IBM_modified.csv', 'MSFT_modified.csv']

url = ['https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true',
'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true',
'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
]

for i, j in zip(csv, url):
    local_path = os.path.join('data', i)
    with urlopen(j) as file, open(local_path, 'wb') as f:
        f.write(file.read())


#GOOGLE
import csv
GOOG = open('data/GOOG.csv', 'r')
csv_GOOG = csv.reader(GOOG)

list_GOOG = []
for row in csv_GOOG:
    list_GOOG.append(row)

for row in list_GOOG[1:]:
    for k in (1,2,3,4,5,6):
        row[k] = float(row[k])


list_GOOG[0].append('Change')

for i in range(1, len(list_GOOG)):
    list_GOOG[i].append((list_GOOG[i][1]-list_GOOG[i][4])/list_GOOG[i][1]*100)
print(list_GOOG)

with open('data/GOOG_modified.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(list_GOOG)

#IBM
import csv
IBM = open('data/IBM.csv', 'r')
csv_IBM = csv.reader(IBM)

list_IBM = []
for row in csv_IBM:
    list_IBM.append(row)

for row in list_IBM[1:]:
    for k in (1,2,3,4,5,6):
        row[k] = float(row[k])


list_IBM[0].append('Change')

for i in range(1, len(list_IBM)):
    list_IBM[i].append((list_IBM[i][1]-list_IBM[i][4])/list_IBM[i][1]*100)
print(list_IBM)

with open('data/IBM_modified.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(list_IBM)

#MSFT
import csv
MSFT = open('data/MSFT.csv', 'r')
csv_MSFT = csv.reader(MSFT)

list_MSFT = []
for row in csv_MSFT:
    list_MSFT.append(row)

for row in list_MSFT[1:]:
    for k in (1,2,3,4,5,6):
        row[k] = float(row[k])


list_MSFT[0].append('Change')

for i in range(1, len(list_MSFT)):
    list_MSFT[i].append((list_MSFT[i][1]-list_MSFT[i][4])/list_MSFT[i][1]*100)
print(list_MSFT)

with open('data/MSFT_modified.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(list_MSFT)


#Pandas example for GOOGLE

#import pandas as pd
#df = pd.read_csv('data/GOOG.csv')
#pd.set_option('display.max_columns', None)
#df.head()
#df['Perc.Change'] = (df['Open'] - df['Close']) / df['Open']*100
#print(df)
#df.to_csv('data/GOOG_modified.csv', index = False)
