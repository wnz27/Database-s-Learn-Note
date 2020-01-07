## 错误问题记录

### navicat连接不上虚拟机配置的mysql问题
###### 排查方向
1. 网络问题
2. ip输入是否正确
3. 配置虚拟机防火墙允许22，3306， 80端口
4. mysql访问权限修改，先`mysql -uroot -p`登录mysql，然后`use mysql`, 再`update user set Host='%' where User='root';`, 之后`flush privileges;`让权限生效。
再重连试试，应该解决问题了。

### MySQL 1045 错误解决访问异常
###### 错误代码:
`pymysql.err.OperationalError:(1045, u"Access denied for user'root'@'192.168.1.10'(using password: YES)")`
###### 解决排查方向：
1. 确认密码是否正确。
2. 确认是否有对IP的授权，%控制允许访问客户端范围，这个不包括localhost。
3. 网络是否畅通。

### MySQL 1153 错误解决访问异常
###### 错误代码：
`pymysql.err.InternalError:(1153, u"Got a packet bigger than 'max_allowed_packet' bytes")`
##### 解决排查方向
1. 增加max_allowed_packet配置的大小
2. 设置为100MB：`SET PERSIST max_allowed_packet=100*1024*1024`，设置GB以此类推。

### MySQL 2002 错误解决连接异常
###### 错误代码
`ERROR 2002 (HY000): Can’t connect to local MySQL server through socket ‘/var/lib/mysql/mysql.sock’ (2)`
###### 错误排查
连接问题
我最初初始化配置mysql服务器的时候，先用的是mysqld --initialize xxxxxxxxxx命令来初始化的，
我的mysql文件位置在`/usr/local/mysql`
之后使用这个命令把启动服务器命令换了位置：`cp /usr/local/mysql/support-files/mysql.sever /etc/init.d/mysqld`
之后可以使用`/etc/init.d/mysqld start`来启动mysql服务
之所以出现上面的错误是因为我忘记启动服务就使用`mysql -u xxxx -p`来登录mysql，所以报错
重新启动服务再登录就没问题了。


