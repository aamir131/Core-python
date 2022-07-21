from array import*
a = array('i',[101,102,103,104])
n = len(a)
i = 0
while i<n:
    print(a[i])
    i+=1
print()
print("After Append metod")
a.append(105)
a.append(106)
m =len(a)
j = 0
while j<m:
    print(a[j])
    j+=1