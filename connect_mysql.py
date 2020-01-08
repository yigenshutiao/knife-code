# coding:utf-8

# 适用于Python3环境

# 屏蔽模块差异
try:
    import MySQLdb as db
except ImportError:
    import pymysql as db

def create_table(conn):
      sql_drop_table = "drop table if exists student"
      sql_create_table = """
            create table student(
            sno int(11) not null,
            sname varchar(255),
            sage int(11),
            primary key(sno)
            )
      """
      execute_sql(conn, sql_drop_table)
      execute_sql(conn, sql_create_table)

# 连接db
def get_conn(**kwargs):
     return db.connect(host=kwargs.get('host', 'localhost'),
                                      user=kwargs.get('user'),
                                      passwd=kwargs.get('passwd'),
                                      port=kwargs.get('port', 3306),
                                      db=kwargs.get('db'))

def execute_sql(conn, sql):
    with conn as cur:
         cur.execute(sql)

def insert_data(conn, sno, sname, sage):
    INSERT_FORMAT = "insert into student value({0},'{1}',{2})"
    sql = INSERT_FORMAT.format(sno, sname, sage)
    execute_sql(conn, sql)

def main():
    conn = get_conn(host="localhost",user="root",passwd="123456",db="test")
    try:
        create_table(conn)
        insert_data(conn, 1,'a', 18)
        with conn as cur:
             cur.execute("select * from student")
             rows = cur.fetchall()
             for row in rows:
                 print(row)
        print("success")
    finally:
        if conn:
           conn.close()

main()
