import mysql.connector

mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'airportkolkata'
)

if mycon.is_connected():
    print(f'DATABASE connected succesfully\n')

cursor = mycon.cursor()

cursor.execute(f'select * from employee')

data = cursor.fetchall()

print(f"overall = {type(data)} and inside = {type(data[0])} \n")

for row in data:
    print(row)