sub = {11:'Python',12:'JAVA',13:'C++',15:'HTML'}
print("Before  Copy")
print(sub)
print(id(sub))
print()

new_sub = sub.copy()

print("After Copy")
print(new_sub)
print(id(new_sub))
print()

sub[11] = 'Advance Python'
print(sub)
print(new_sub)