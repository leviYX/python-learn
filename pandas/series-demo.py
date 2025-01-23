import numpy as np
import pandas as pd

obj = pd.Series([4, 7, -5, 3])
val = obj.values
print(val)

keys = obj.keys()
print(keys)


obj2 = pd.Series(['one', 'two', 'three', 'four'],index=['1', '2', '3', '4'])
print(obj2)
print(obj2['1'])
print("****************************")
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = pd.DataFrame(data)
print(frame)