set1 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set2 = set()
for i in set1:
    new_set2.add(i+1)
print(new_set2)
print()


set2 = {i if (i%2==0) else i*1000 for i in range(10)}
print(set2)