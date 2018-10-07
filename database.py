import mysql.connector
from sqlquery import SqlQuery

def openConnection(userid, password, instance,server="localhost"):
    mydb = mysql.connector.connect(
         host=server,
         user=userid,
         passwd=password,
         database = instance
         
    )
    return mydb

connection = openConnection(userid='spring', password='spring', instance='python')
sql = SqlQuery("SELECT * FROM SAMPLE",connection)
sql.addConstraint("idsample", "=", 4, 3)
sql.prepare()
for result in sql.query():
    print(result) 
#connection = openConnection(userid='spring', password='spring', instance='python')
#cursor = connection.cursor()
#cursor.execute("select * from sample")
#res = 1
#while  res != None :
 #   res = cursor.fetchone()
 #   if res != None:
 #       print(res)

 
