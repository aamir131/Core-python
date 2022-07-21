print("cloning mthod")
a=[78,88,55,34]
b=a[:]
print("A: ",a)
print("B: ",b)
b[2] = 90
print()
print("A: ",a)
print("B: ",b)
print()



print("Copy method")
c=[67,5,90,34,2]
d=c.copy()
print("C: ",c)
print("D: ",d)

c[1]=70
print()
print("C: ",c)
print("D: ",d)