sub = {11:'Python',12:'JAVA',13:'C++',15:'HTML'}
print("Original dict:")
print(sub)
print()

all_value = sub.values()
print(all_value)
print(type(all_value))
print()

values_lst = list(all_value)
print(values_lst)
print(type(values_lst))
print()
for v in values_lst:
    print(v)