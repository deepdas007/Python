mylist = []
mylist.append(5)
mylist.append(10)
mylist.append(15)
mylist.append(20)
mylist.append(3)
mylist.append(30)
mylist.append(13)
print(mylist)
print()

mylist.insert(1,8)
print(mylist)
print()

print(mylist.index(3))
print()

mylist.reverse()
print(mylist)
print()

mylist.sort()
print(mylist)
print()

mylist.insert(1,3)
mylist.insert(1,3)
print(mylist)
print()

mylist.remove(3)
print(mylist)
print()

del mylist[3]
print(mylist)
print()

l = "     Hello World"
r = "Hello World         "
a = "           Hello World            "

lgone = l.lstrip()
print(lgone)
print()

rgone = r.rstrip()
print(rgone)
print()

agone = a.strip()
print(agone)
print()