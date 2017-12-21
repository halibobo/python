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
