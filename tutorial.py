import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)


mycursor = db.cursor
mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("DESCRIBE Person (name, age) VALUES (%s,%s)", ("Joseph", 17))
db.commit()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print (x)
