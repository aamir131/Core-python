from numpy import*
m =int(input("Enter Number of rows: "))
n =int(input("Enter Number of columns: "))
a = ones((m, n),dtype= int)
u = len(a)
print(a)
i =0
while(i<u):
    j = 0
    while(j<len(a[i])):
        x = int(input("Enter elements: "))
        a[i][j] = x
        j+=1
    i+=1
i =0
while(i<u):
    j =0
    while(j<len(a[i])):
        print(a[i][j])
        j+=1
    i+=1
print()
print(a)
