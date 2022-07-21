a = {}
n = int(input("Enter number of Elements: "))
for i in range(n):
    k = input("Enter Key: ")
    v = input("Enter VAlue: ")
    a.update({k:v})
print(a)