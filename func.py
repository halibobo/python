def square(r):
	if not isinstance(r,(int,float)):
		raise TypeError("error type!")
	return 3.14*r*r

print(square(5))

# print(square('s2'))

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)


def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,3))
print(power(6))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city+'\n')

enroll('jack',5)
enroll('lucy',4,12)
enroll('lily',12,city="NewYork")


def add_last(l=[]):
	l.append('last')
	print(l)
	return l

add_last()
add_last() #定义默认参数要牢记一点：默认参数必须指向不变对象！

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,4]))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,12))
nums = [1, 2, 3]
print(calc(*nums)) #*nums表示把nums这个list的所有元素作为可变参数传进去


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Michael', 30,a=('123',"456"),v=12)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("liye",43,**extra)


#不受限制的关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


#只接收city和job作为关键字参数。无初始值必须传递
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, city='NanJing', job='code')
person('Bill', 14, job='plan')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1,2,3,'a', 'b',2)
f1(1,2,3,'a', 'b',3,key="keyword")

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)