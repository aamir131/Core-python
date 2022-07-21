def show(d):
    print(d)
    print(type(d))
    for i in d:
        print(i, "=", d[i])

dc  = {'course':'Python','fees':30000}
show(dc)