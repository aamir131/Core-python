a = 50
def sho():
    
    print("Local variable: ",a)
    x = globals()['a']
    
    print("x :")
    x = 30
    print("X : ",x)


sho()
print("Global variables: ",x)