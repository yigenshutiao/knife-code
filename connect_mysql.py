try:
    import MySQLdb as db
except ImportError:
    import pymysql as db


def create_table(conn):
    sql_drop_table = "drop table if exisets student"
    sql_create_table = """
            create table 'student'(
            sno int(11) not null,
            sname varchar(255),
            sage int(11),
            primary key(sno)
            )engine=innodb defeault charset=utf8mb4
      """


def get_conn(**kwargs):
    return db.connect(host=kwargs.get('host', 'localhost'),
                      user=kwargs.get('user'),
                      passwd=kwargs.get('passwd'),
                      port=kwargs.get('port', 3306),
                      db=kwargs.get('db'))


def execute_sql(conn, sql):
    with conn as cur:
        cur.execute(sql)


def insert_data(conn, son, sname, sage):
    INSERT_FORMAT = "insert into student value({0},{1},{2})"
    sql = INSERT_FORMAT.format(sno, sname, sage)
    execute_sql(conn, sql)


def main():
    params = {"host": "localhost", "user": "root", "passwd": "123456", "port": "3306", "db": "test"}
    conn = get_conn(params)
    try:
        create_table(conn)
        insert_data(conn, 1, 'a', 18)
        with conn as cur:
            cur.execute("select * from student")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    finally:
        if conn:
            conn.close()


main()
