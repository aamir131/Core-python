from numpy import*
a = zeros((3, 2), dtype=int)
for b in a:
    for j in b:
        print(j)
    print()
print()
d = ones((3, 2), dtype=int)
n = len(d)
i = 0
while(i<n):
    f = 0
    while(f<len(d[i])):
        print(d[i][f])
        f+=1
    i+=1
        

