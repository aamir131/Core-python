a = (10,20,30,50,(60,70))
n = len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])
print()
c = ((11,22,33),(44,55,66))
l = len(c)
for p in range(l):
    for d in range(len(c[p])):
        print(p,d,c[p][d])
    print()