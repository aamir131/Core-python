x = [[10,20,30],
[40,50,60],
[70,80,90],
[11,22,33],
[44,55,66],
[77,88,99],
[12,13,14]]

print("Originali List")
print(x)
print()
print("From 1st Position to 4th Position")
a = x[1:5]
print(a)
print()
print("From 0th Position to last Position")
b = x[0:]
print(b)
print()
print("From 0th to 4th Position")
c = x[:5]
print(c)
print()
print("Last 4th Position")
d = x[-4:][1][1]
print(d)
print()
print("From 0th Position to 6th Position stepsize 2")
e = x[0:7:2]
print(e)