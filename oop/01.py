
'''
定义一个空的类
'''
class student():
    # 一个空类,pass代表直接跳过
    # 此处psaa必须有
    pass
# 定义一个对象
mingyue = student()

# 再定义一个类,用来描述听python的学生
class pythonstudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "python"
    # 注意
    # def dohomework的缩进层级
    # 系统默认一个self参数
    def dohomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yhueyue的学生,是一个具体的人
yueyue = pythonstudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员幻术的调用没有传递进入参数
yueyue.dohomework()