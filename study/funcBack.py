#funcBack.py

def lazzy_sum(*arg):
    def sum():
        s = 0
        for n in arg:
            s = s + n
        return s
    return sum
f = lazzy_sum(1,3,6,2,6,9,12)
print(f)
print(f())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print('f1',f1())
print('f2',f2())
print('f3',f3())
        

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
print('f1',f1())
print('f2',f2())
print('f3',f3())

def createCounter():
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
