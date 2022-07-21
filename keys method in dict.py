sub = {11:'Python',12:'JAVA',13:'C++',15:'HTML'}
print("Original dict:")
print(sub)
print()

all_key = sub.keys()
print(all_key)
print(type(all_key))

print()
keys_lst = list(all_key)
print(keys_lst)
print(type(keys_lst))
for i in keys_lst:
    print(i)