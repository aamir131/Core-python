from numpy import*

def show(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar
    print()

a = array([121,234,202,205,301,401])
y = show(a)
print("Returning array: ",y)
print(type(y))
for i in y:
    print(i)