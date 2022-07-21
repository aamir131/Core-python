# delete using slicing and concatnation
a = (10,20,30,40.78,-50,'Mak')
print(a)  # suppose i delete 30 in tuple
s1 = a[0:2] 
s2 = a[3:]
tup = s1+s2
print(tup)