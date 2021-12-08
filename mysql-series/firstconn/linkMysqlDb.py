import pymysql

conn=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="testdb",
        charset='utf8')
cur=conn.cursor()

cur.execute("select version()")
data = cur.fetchone()
print("Mysql/Maria db version: %s"%data)

conn.close()
