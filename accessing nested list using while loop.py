a = [10,20,30,[40,50]]
n = len (a)
i = 0
while i<n:
    if type(a[i])is list:
        if len(a[i])>1:
            m = len(a[i])
            j = 0
            while j<m:
                print(i,j,a[i][j])
                j+=1
            i+=1
    else:
        print(i,a[i])
        i+=1 
print()

b  = [[11,22,33],[44,55,66]]
n = len(b)
i = 0
while i<n:
    j = 0
    while j<len(b[i]):
        print(i,j,b[i][j])
       
        j+=1
    i+=1