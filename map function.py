a = [10,20,30,40,50]
b = [1,2,3,4,5]

result = list(map(lambda x,y:(x+y),a,b))

for i in result:
    print(i)
print(type(result))