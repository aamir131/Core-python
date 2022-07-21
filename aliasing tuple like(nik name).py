a = (10,20,30,40,50)
b = a
a = a[:3]
print(a)
print(id(a))
print(b)
print(id(b))