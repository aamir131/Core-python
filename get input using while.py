from array import*
name = array('i',[])
n = int(input("Enter no. of Element: "))
i =0
j= 0
while(i<n):
    name.append(int(input("Enter Element: ")))
    i+=1
while(j<len(name)):
    print(name[j])
    j+=1
