from sys import getsizeof
a = 32
b = 34.55
c = "Mak"
d = [10,20,30]
e = (10,20,30)
f = {10,20,30}
g = {10:'C',20:'B',30:'A'}
#type
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))
print(getsizeof(d))
print(getsizeof(e))
print(getsizeof(f))
print(getsizeof(g))