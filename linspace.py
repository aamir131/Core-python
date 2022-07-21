from numpy import*
a = linspace(1,8,5)
n =len(a)
for i in range(n):
    print(i,"=",a[i])
print("###################################")
n = len(a)
i = 0
while(i<n):
    print(i,"*",a[i])
    i+=1
