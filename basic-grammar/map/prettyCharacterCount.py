import pprint
import random

names = ["levi","tom","jerry","jack","fuck"]
def initMap():
    res = {}
    for i in range(10):
        res[i] = names[random.randint(0,len(names)-1)]
    return res
res = initMap()
print(res)
pprint.pprint(initMap())