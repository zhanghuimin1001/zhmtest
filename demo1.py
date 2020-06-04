# b=18
# if b > 8:
#     print("成年人")
# else:
#     print("未成年人")

# a="儿童节"
# c="快乐儿童节"
# d="儿童节快乐"
# f=["快乐儿童节","儿童节"]  #数组里面如果没有一模一样的"儿童节"，就不能a in f 
# if a in f:
#     print("青蒿")
# else:
#     print("九思")


# g="哥哥"
# h="妹妹"
# j="哥哥"
# if g is j:    
#     print("青蒿")
# else:
#     print("九思")
# ==判断两个变量的值是否相等
# is判断两个变量的值和内存地址是否相等


# a = 1
# b = 2
# c = 3
# if c > b or b > c:       #and是并且，or是或者
#     print("王一波")
# else :
#     print("错了")



# a = [1,2,3,4]
# for i in a :   #for中的in不是判断
#     print(i)



# d =  {"name":"李四","password":"123321"}
# for i in d :
    # print(i)            #第一次循环name
    # print(d[i])         #key值方式取值
    # print(d.get[(i))    #get方式取值
    # print("==========")
#d["张三"]和d.get("张三")的区别：如果键值对不存在，get取空值，key值会报错
# a = d.get("张三")
# print(a)
# b=d["张三"]
# print(b)

"""
db =[
   {"name":"张三","password":"123123"},
    {"name":"李四","paassword":"123321"}
]
zh = input("请输入账号:")
mm = input("请输入密码:")
for 中的i：就是这个{"username":"张三", "password":"123456"}
# 再用for a in i：意思就是去i这个字典中 去key和value， i就是a， i,get(a)就是对应的value
for i in db :
    if zh == i.get("name") and mm == i.get("password"):
        print("输入的账号{}登陆成功！".format(zh))
    else:
        print("登陆失败！")

if 1 == 2:
    if 2 ==2:
        print("1")
    else:
        print("2")
else:
    print("3")

"""

# db =  [
#     {"name":"李四","password":"123321"},
#     {"name":"王五","password":"123456"}
#     ]

# zh = input("请输入账号:")
# mm = input("请输入密码:")
# # count = 1
# for i in db:
#     if zh == i.get("name"):
#         i.update("password") = mm
        # i["password"] = mm
    #     break
    # else:
    #     if len(db) == count:
    #         db.append({"name":zh,"password":mm})
    # count = count +1
    # #    c = {}
    #    c["name"] = zh
    #    c["password"] = mm
    #    db.append(c)
# print(db)


#数组[]里面是列表，不可以使用get取值，字典里面是键值对，可以使用get取值
#取值有两种： i.get("name") 和  i["name"] 
# a={"u":"123"}
# a["u"]=456   # key键值对  读写，可以赋值
# a.get("u")   # get取值    只能读