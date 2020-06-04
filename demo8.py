# 模拟管理员登录
from dbtools import chaxun
from dbtools import commit

# 登录的例子
# username = input("请输入账号:")
# password = input("请输入密码:")

# sql = 'select * from t_admin where username="{}" and password="{}"'.format(username, password)
# res = chaxun(sql)

# # 有结果
# if len(res) != 0:
#     print("管理员登录成功！")
# else:
#     print("管理员登录失败！")


# -------------------------- 注册的例子 ---------------------------
username = input("请输入账号:")
password = input("请输入密码:")

sql = 'INSERT into t_admin values(NULL, "{}", "{}", NULL, NULL, "管理员2", "好好学习啊", "headimg.jpg", NULL, "女", 0, NULL, NULL, NULL)'.format(username, password)
res = commit(sql)
if res == True:
    # 写一个查询改账号是否注册成功，账号在不在数据库里面
    print("注册成功！")
else:
    print("注册失败！")