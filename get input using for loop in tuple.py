# getting input from user in tuple
a = []
n = int(input("Enter no of Elements: "))
for i in range(n):
    a.append(int(input("Enter Elements: ")))

print(type(a))

a = tuple(a)
print(type(a))
for i in a:
    print(i)