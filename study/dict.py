dict = {"a":1,'b':2,"c":[1,'sa']}
print('a,',dict['a'])
print(("d" in dict))

print(dict.get("c"))
print(dict.get("f"))


#在set中，没有重复的key
s = set([1,2,4,2,4,5,6,7])
print(s)
s.add(3)
print(s)
print(7 in s)
s.remove(7)
print(s)


a = ['e','c','a']
a.sort()
print(a)

str = "addaadad"
print(str.replace('a','B'))