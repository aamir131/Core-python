sub = {11:'Python',12:'JAVA',13:'C++',15:'HTML'}
print("Original dict:")
print(sub)
print()
it = sub.items()
print(it)
print(type(it))
print()

lst = list(it)
print(lst)
print(type(lst))
print()

for i in lst:
    for j in i:
        print(j)

print()
tup = tuple(lst)
print(tup)