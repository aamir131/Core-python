stu = {101:'Rahul',102: 'Python',103:'JAVA'}
print("Before Modification")
print(stu)
print(id(stu))
print()

print("After Modification")
stu[101] = "Advance Python"
print(stu)
print(id(stu))