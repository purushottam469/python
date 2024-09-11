import mysql.connector

connection=mysql.connector.connect(
   bd_name="dbname",user="root",password="ss22g",host="local-host",port=6363
)
_cursor=connection.cursor()
_cursor.execute(
    
    "CREATE TABLE employee (eid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,phone VARCHAR(15) NOT NULL);"
)
    
connection.close()
      