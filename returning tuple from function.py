def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
    return t

tup = (10,20,30,40.84,'Mak')
new_tup = show(tup)
print()
print(new_tup)
print(type(new_tup))