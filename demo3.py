class person():
    name = "王一波"
    sex = "男"
    age =  "22"

    def see(self):    
        print("{}看电影了".format(self.name))

    def hear(self,music):
        print("{}听{}".format(self.name,music))
        return "music"
#self代表类本身，

s = person()
# print(s.age)
# print(s.sex)
# print(s.name)
a = s.see()
p = s.hear("音乐")
print(p)
print(a)
