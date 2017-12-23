from functools import reduce

f = abs
print(f(-40))

def funcAdd(a,b,f):
    return f(a)+f(b)

print(funcAdd(1,-4,abs))
print(funcAdd(1.8,9.9,int))

def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8])
print(r)
print(list(r))


def add(x,y=3):
    return x+y

r = map(add,[1,-2,2,4])
print(list(r))
print(reduce(add,[1,2,3,4]))

def fn(x,y):
	return x*10+y
print(reduce(fn,[7,2,4,6,7]))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('155626'))

def char2num(s):
    return DIGITS[s]
def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('98652665'))
  


def prod(L):
    def ji(x,y):
        return x*y
    return reduce(ji, L)
#or
def prod(L):
    return reduce(lambda x, y: x*y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


import math
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    integerstr = s.split('.')[0]
    decimalstr = s.split('.')[1]
    def chartonum(s1):
        return DIGITS[s1]
    def tointeger(x,y):
        return x*10+y
    p1 = reduce(tointeger,map(chartonum,integerstr))
    p2 = reduce(tointeger,map(chartonum,decimalstr))/(math.pow(10,len(decimalstr)))
    return p1+p2

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

def is_odd(n):
    return n % 2 == 1
l = list(filter(is_odd,range(20)))
print(l)

def is_empty(s):
    return s and s.strip()
l = list(filter(is_empty,['1','3',None,'23','as0','']))
print(l)

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')



testArray = [5,5,-844,89,-99,-22,2,7,41]
s = sorted(testArray)
print(s)
s= sorted(testArray,key=abs)
print(s)

testArray = ['Atsd','bada','djda','gxda','ccda','zvdsaa','geeas']
def sortedStr(s):
    return s[1:2]
s = sorted(testArray,key=sortedStr)
print(s)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return str.lower(t[0])
def by_store(t):
    return t[1]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_store)
print(L2)
print(L3)