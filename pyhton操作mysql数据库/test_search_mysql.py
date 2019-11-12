#! -*- encoding=utf-8 -*-
import pymysql

class MySearchSQL(object):
    def __init__(self):
        self.get_connect()
    def get_connect(self):
        try:
            self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="1030",
            db="news",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        except pymysql.Error as e:
            print('Error: %s' % e)
    
    # 关闭连接
    def close_connect(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('Error: %s' % e)
    
    def get_one(self):
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `types` DESC;'
        # 找到cursor
        # 执行SQL
        # 拿到结果
        # 处理数据
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(sql, ('百家',))
                result = cursor.fetchone()
                # print(dir(cursor))
                print(cursor.description)
                print(result)
                print(result['title'])
                pass
            except Exception as e:
                print(e)
            # 关闭cursor
            cursor.close()
    
    # 执行sql
    def executeSQL(self,sql):
        with self.conn.cursor() as cursor:
            try:
                result = cursor.execute(sql)
                print(result)
                # 打印结果
                rows = cursor.fetchall()
                print(cursor.description)
                print(rows)     # 装每条数据的列表
                for row in rows:
                    print(row)
                cursor.close()
            except pymysql.Error as e:
                print('Error: %s' % e)
    
def main():
    # 准备sql
    sql = 'SELECT * FROM `news`;'
    connect = MySearchSQL()
    # 执行sql
    # connect.get_one()
    connect.executeSQL(sql)
    # 关闭连接
    connect.close_connect()


if __name__ == "__main__":
    main()
'''
还可以用LIMIT来模拟页数，offset 和 page_size
用page来替代offset
offset = (page-1) * page_size
'''


