sub = {11:'Python',12:'JAVA',13:'C++',15:'HTML'}
print("Original dict:")
print(sub)
print(id(sub))
print()

new = {'Name':'Aamir','Address':'Mumbai','Pin':65443}

sub.update(new)
print("Update dict:")
print(sub)
print(id(sub))
print()