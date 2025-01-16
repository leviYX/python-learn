import numpy as np

# 生成2行3列的小数二维数组
data = np.random.randn(2, 3)
print(data)
print("*********************")

data1 = [1,2,4.5,7,9]
array1 = np.array(data1) # [1.  2.  4.5 7.  9. ] 当你的数据中有小数比如4.5的时候，此时就会给你格式化为浮点数，每一个输出的元素后面都有一个.来标识浮点数
print(array1)
print(f"array1的大小是{array1.shape},他的元素类型是{array1.dtype}")
array1 = array1.astype(int) # 格式化为整数
print(array1)
print(f"array1的大小是{array1.shape},他的元素类型是{array1.dtype}")

print("*********************")
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
array2 = np.array(data2)
print(array2)