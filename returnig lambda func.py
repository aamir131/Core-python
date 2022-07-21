def add():
    x = 34
    return (lambda y: y+x)
a = add()
print(a(16))
