from array import*
roll = array('i',[101,102,103,104,105])
n = len (roll)
i=0
while(i<n):
    print(roll[i])
    i+=1


print("array after reverse")
roll.reverse()
a = len(roll)
j=0
while(j<a):
    print(roll[j])
    j+=1
