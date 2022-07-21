from numpy import*
n = int(input("Enter number of Element: "))
a = zeros(n,dtype=int)
u = len(a)
i = 0
j = 0
while(i<u):
    x = int(input("Enter lement1: "))
    a[i]= x
    i+=1
while(j<u):
    print(a[j])
    j+=1
