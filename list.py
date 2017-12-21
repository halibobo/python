array = ['a','b','sasd']
leng = len(array)
print(len(array))
print(array[leng-1])
print(array[-1])

array.append('增加阿达')
print(array)

array.insert(1,"插入一条")
print(array)

lastItem = array.pop() #取末尾
print("最后一条：",lastItem)

array.pop() #删除最后一条
print('删除最后一条：',array) 

#混合类型的数组
hybirdArray = ['str',12,1.5,array]
print('混合类型：',hybirdArray)


#不可修改的 tuple
tupleData = ('第一天','第二天','第三条')
print("tuple data : ",tupleData)

temp = (1,'a','b',['c','d'])
temp[3][0] = 'q'
print(temp)