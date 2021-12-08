import pymysql
def getCursor():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="testdb",
        charset='utf8')
    cursor=db.cursor()
    return cursor
def selectAll(cur):
    cmd="select * from employee"
    try:
        cur.execute(cmd)
        data=cur.fetchall()
        for row in data:
            print("|",end='')
            for one in row:
                print(one,end='\t| ')
            print()
    except:
        print("select failed")
        raise
