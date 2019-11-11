#! -*- encoding=utf-8 -*-
import pymysql

def get_connect(self):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="1030",
        db="news",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn


# 准备sql
sql = 'SELECT * FROM `news`;'
# 执行sql
with conn.cursor() as cursor:
    try:
        result = cursor.execute(sql)
        print(result)
        # 打印结果
        rows = cursor.fetchall()
        print(cursor.description)
        for row in rows:
            print(row)
    except pymysql.Error as e:
        print('Error: %s' % e)