a = (10,20,30,[40,50])
print("Original Tuple A: ",a)
print(id(a))
print(type(a))
print()
n = len(a)
for i in range(n):
    if type(a[i])is list:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])
print()
c = ([11,22,33],[44,55,66])
u = len(c)
for i in range(u):
    for j in range(len(c[i])):
        print(i,j,c[i][j])
    print()
