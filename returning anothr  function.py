def disp():
    def show():
        return "Disp function"
    print("Show function")
    return show
ass = disp()
print(ass())
print()
def old(sd):
    print("old function")
    return sd
def new():
    return "new function"
sa = old(new)
print(sa())
