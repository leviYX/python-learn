import time

import numpy as np


my_array = np.arange(100_000_000)
my_list = list(range(100_000_000))

start_time = time.time()
for _ in range(10):
    my_array2 = my_array * 2

print(f'numpy一亿数组循环10遍，每次操作都乘以2，一共耗时{time.time() - start_time}秒')


start_time = time.time()
for _ in range(10):
    my_list2 = my_list * 2

print(f'python一亿数组循环10遍，每次操作都乘以2，一共耗时{time.time() - start_time}秒')
