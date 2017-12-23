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


