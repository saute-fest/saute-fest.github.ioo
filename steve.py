import sqlite3

connection = sqlite3.connect("remotemysql.com") 
#connecting to the SQL database ^
crsr = connection.cursor() 

crsr.execute("SELECT * FROM remotemysql.com")  

# store all the fetched data in the ans variable 
ans= crsr.fetchall()  
  
# loop to print all the data 
for i in ans: 
    print(i)   