import csv
import pymssql

i = 0

conn = pymssql.connect(server="127.0.0.1", user='root', password='root', database='pv_data')

cur = conn.cursor()

file = open('usable_data.csv')
csv_data = csv.reader(file)

skipHeader = True

for row in csv_data:

    if skipHeader:
        skipHeader = False
        continue
#    cur.execute('INSERT pv-werte (Zeit, ETotal, PAC, PDC)' 'VALUES(%s, %s, %s, %s)' row)
cur.execute('INSERT pv-werte (Zeit, ETotal, PAC, PDC)', 'VALUES(i + 1,%s, %s, %s, %s)', row)
cur.close()
conn.close()
