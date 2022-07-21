# passing array to function
from array import*

def show(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)
a = array('i',[121,234,202,205,301,401])

show(a)