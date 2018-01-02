class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(std):
        print('%s:%s' % (std.name,std.score))

stu = Student("aa",56)
stu.print_score()
print(stu.name)