tupe2List = list(("levi","tom"))
print(tupe2List)

def tupe2List(tupe):
    return list(tupe)

def list2Tupe(lst):
    return tuple(lst)

print(list2Tupe(["1","2"]))
print(tupe2List(("1","2")))