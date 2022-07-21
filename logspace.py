from numpy import*
a = logspace(2,3,5,base=12)
for i in a:
    print(i)

print()
print()
n = len(a)
i =0
while(i<n):
    print(i,"==",a[i])
    i+=1

