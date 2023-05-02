import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yourpassword",
  database="yourdatabase"
)
mycursor=mydb.cursor()

# Show all Tables 

mycursor = mydb.cursor()
mycursor.execute("Show Tables")
for i in mycursor:
    print(i)
mycursor.close()

# Create Table

tabname=input("Enter Table Name :")
query="Create Table {} (Titles varchar (255),Duration varchar(225))".format(tabname)
mycursor.execute(query)
print("Table",tabname,"Table Created Succesfully ! ")
mydb.close()

# Create Table with  primary key 

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(100))")