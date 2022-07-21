a = [10,20,30,40,[50,60]]
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
f = [[32,44,55],[12,34,57]]
n=len(f)

for i in range(n):
    m=len(f[i])
    for j in range(m):
        print(i,j,f[i][j])
    print( )

  
