def cal(lst):
    print("IFBA: ",lst,id(lst))
    lst=[11,22,43]
    print("IFAA",lst,id(lst))

lst = [1,2,3]
print("BCF: ",lst,id(lst))
cal(lst)  
print("ACF: ",lst,id(lst))