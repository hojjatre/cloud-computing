import sqlite3
import csv

conn = sqlite3.connect('vgsales.db.sqlite3')

insert_records = "INSERT INTO main_service_vgsales (Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_sales, Global_Sales) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor = conn.cursor()

file = open('vgsales.csv')
 

contents = csv.reader(file)

cursor.executemany(insert_records, contents)



conn.commit()
conn.close()