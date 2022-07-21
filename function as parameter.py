def disp(sy):
    return "disp function" + sy()
    
def show():
    return" show function"
d = disp(show)
print(d)
