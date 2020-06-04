class person():
    name = "王一波"
    sex = "男"
    age =  "22"
    def see(self):
        print("看电影了")
    def hear(self,music):
        print("听{}".format(music))
        return "听音乐了"
s = person()
# print(s.age)
# print(s.sex)
# print(s.name)

p = s.hear("音乐")
print(p)
