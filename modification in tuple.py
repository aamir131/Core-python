a = (10,20,30,40,-50,'Mak')
s1 = a[:2] #this slicing
s2 = a[2:] #this slicing
c = (101,102)
print(s1)
print(s2)
print(c)
print()
tup = s1+c+s2 #this is concatnation not a modification
print(tup)