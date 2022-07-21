dict = {'name':'Aamir',1:{}}
print("Before Modification:")
print(dict)


print()

del dict['name']
print("After modification")

dict['course'] = 'Python'
dict['course1'] = 'JAVA'
dict['course2'] = 'CSS'

print(dict)
dict[1]['fees1'] = 10000
dict[1]['fees2']  = 20000
dict[1]['fees3'] = 30000
print(dict[1])