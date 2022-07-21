def show(a,b):
    yield a
    yield b
result = show(10,20)
print(result)
print(type(result))
print(next(result))
print(next(result))

print()
def disp(x,y):
    while x<=y:
        yield x
        x+=1
result=disp(1,5)
print(result)
print(next(result))
print(next(result))
print()
for i in result:
    print(i)