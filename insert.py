import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values (123,'nikhil',245.253,125,'bagul')")
mycursor.execute("insert into test2.test_table values (123,'nikhil',245.253,125,'bagul')")
mycursor.execute("insert into test2.test_table values (123,'nikhil',245.253,125,'bagul')")
mycursor.execute("insert into test2.test_table values (123,'nikhil',245.253,125,'bagul')")
mydb.commit()
mydb.close()