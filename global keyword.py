i = 0
def fun():
    global i
    while i<5:
        i+=1
        print(i)
fun()
print(i)
