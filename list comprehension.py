ls = []
for i in range(10):
    if(i%2==0):
        ls.append(i)
    else:
        ls.append("Invalid")
#print(ls)
# with list comprehension
lst = [i if(i%2==0) else "Inavalid" for i in range(10)]
print(lst)