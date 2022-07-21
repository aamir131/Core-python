dict = {}
for n in range(10):
    if(n%2==0):
        if(n%3==0):
            dict[n] = n*2
        
print(dict)

dict2 = {n:(n if n%2==0 else "Invalid") for n in range(10)}
print(dict2)

print()
lst = ([101,'rahul'],[102,'raj'])
dict33 = {k:v for k,v in lst}
print(dict33)
