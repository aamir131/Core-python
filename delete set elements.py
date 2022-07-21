a = {10,20,30,40,'Mak',50}
print("Before Removing Elements: ",a)
print(type(a))
print(id(a))
print()
a.remove('Mak')
print("After Removing Elements in remove method: ",a)
print(id(a))

print()
a = {11,22,33,44,'Mak',50}
print("Before Removing Elements discard: ",a)
print(type(a))
print(id(a))
print()
a.discard('nak')
print("After Removing Elements in discard method: ",a)
print(id(a))