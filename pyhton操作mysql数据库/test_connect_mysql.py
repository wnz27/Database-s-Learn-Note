#! -*- encoding=utf-8 -*-
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="1030",
    db="news",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with conn.cursor() as cursor:
        # Read a single record
        sql = 'SELECT * FROM `news` ORDER BY `title` DESC;'
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
except pymysql.Error as e:
    print('Error: %s' % e)
finally:
    conn.close()