a = (10,20,30,40,(50,60,70))
n = len(a)
i = 0
while i<n:
    if type(a[i]) is tuple:
        if len(a[i])>1:
            j = 0
            m = len(a[i])
            while j<m:
                print(i,j,a[i][j])
                j+=1
            i+=1
    else:
        print(i,a[i])
        i+=1
print()
b = ((11,22,33),(44,55,66))
u = len(b)
i = 0
while i<u:
    j = 0
    v = len(b[i])
    while j<v:
        print(i,j,b[i][j])
        j+=1
    i+=1