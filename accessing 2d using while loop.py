from numpy import*
a = array([[10,22,33,44],[50,55,66,77]])
n = len(a)
i = 0
while(i<n):
    
    j = 0
    while(j<len(a[i])):
        print(i,j,"=",a[i][j])
        j+=1
    i+=1
    print()
