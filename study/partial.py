#partial
print('ss')
print(int('2116'))
print(int('2116',base=16))
print(int('01110',base=2))

def int2(i):
    return int(i,base=2)
print(int2('11010'))

import functools
int2 = functools.partial(int,base=2)
print(int2('11010'))

int3 = functools.partial(int2,10)