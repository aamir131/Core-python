def show(d):
    print(d)
    print(type(d))
    for i in d:
        print(i, "=", d[i])
    return d

dc  = {'course':'Python','fees':30000}
new_dc = show(dc)
print(new_dc)
print(type(new_dc))