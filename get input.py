from array import*
name = array('i',[])
a = int(input("Enter no. of element"))
for i in range(a):
    name.append(int(input("Enter Element")))
for i in range(len(name)):
    print(name[i])
