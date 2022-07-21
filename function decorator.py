def decor2(num):
    def inner():
        s = num()
        multi = s*5
        return multi
    return inner


def decor1(num):
    def inner():
        e=num()
        add=e+10
        return add
    return inner



def decor(num):
    def inner():
        d = num()
        di= d/2
        return di
    return inner
    

# @decor
# @decor1
# @decor2

def num():
    return 10
num = decor(decor1(decor2(num)))
print(int(num()))