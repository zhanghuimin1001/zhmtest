import pymysql

def chaxun(sql):
    """
        查询数据mysql数据库:只能select，不要delete update insert
    """
    # pymysql 连接数据库
    # host="192.144.148.91":数据库的ip地址 user="ljtest"：数据库登录账号, password="123456"：密码, db="ljtestdb"：数据库名字
    db = pymysql.connect(host="203.195.155.56", user="root", password="123456", db="ljtestdb")
    # 获取游标 ：查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 得到执行的结果
    res = cur.fetchall()
    db.close()
    return res

# sql = "select * from t_user where id = 103468"
# a = chaxun(sql)
# print(a)


 
def commit(sql):
    """
        增加/删除/修改方法：delete update insert：不要传select
    """
    
    # 打开数据库
    db = pymysql.connect(host="203.195.155.56", user="root", password="123456", db="ljtestdb")
    # 获取游标 ： 查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 提交修改 
    db.commit()
    db.close()
    return True

#修改
# update
# sql = "update t_user set username='mcc1234' where id=103468"

#新增
# insert
sql = 'INSERT into t_admin values(123, "zhangsan", "123123", NULL, NULL, NULL, NULL, "12315814521",  "女",0, NULL, NULL, NULL)'

# 删除
# delete
# sql = "delete from t_admin where id=121"
commit(sql)

   