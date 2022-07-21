a = [(10,20,30),(40,50)]
print("Original Lisat A: ",a)
print(id(a))
print(type(a))
print()
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])