sub = {11:'Python',12:'JAVA',13:'C++',15:'HTML'}
print("Original dict:")
print(sub)
print(id(sub))
print()

return_value = sub.setdefault(14,'ASP.NET')
print("After setdefault dict:")
print(sub)
print(id(sub))
print()
print("Return value",return_value)