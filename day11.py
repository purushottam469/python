# databases

import  sqlite3 #  file based database

connection=sqlite3.connect("student.db")

_cursor=connection.cursor()

try:
  _cursor.execute("create table student (name,roll_no,grade)")

except sqlite3.OperationalError as e:
  print(str(e))
  pass

# _cursor.execute("insert into student values('ram',21,2)")
# connection.commit()
result=_cursor.execute("select * from student")
print(result)

for row in result:
  print(row)

