L = ['Bill','Jack','jone','Dear','Func','Slice']

def getItems(n):
    items = []
    for i in range(n):
        items.append(L[i])
    return items

print(getItems(2))

#Slice 切片
print(L[0:2])
print(L[-2:])
print(L[-2:-1])
print(L[:1])
print('前10个数，每2个取一个',L[:10:2])


# 练习
def normalize(name):
    return name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


