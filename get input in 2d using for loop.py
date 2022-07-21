from numpy import*
m =int(input("Enter Number of rows: "))
n =int(input("Enter Number of columns: "))
a = zeros((m, n),dtype= int)
u = len(a)
print(a)
for i in range(u):
    for j in range(len(a[i])):
        x=int(input("Enter a Elements: "))
        a[i][j] = x
for r in a:
    for c in r:
        print(c)
print(a)

