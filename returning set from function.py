def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s
st = {10,20,30,'Mak',50}
ne_st = show(st)
print(ne_st)
print(type(ne_st))