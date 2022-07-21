from array import*
roll = array('i',[101,102,103,104,105,102])
n = len(roll)
i=0
while(i<n):
    print(roll[i])
    i+=1

print("after remove method")
r = roll.remove(101)

p = len(roll)
j=0
while(j<p):
    print(roll[j])
    j+=1
print()
print(r)
