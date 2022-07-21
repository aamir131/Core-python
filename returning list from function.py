def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l

list = [12,76,90,45]
new=show(list)
print(new)
print(type(new))