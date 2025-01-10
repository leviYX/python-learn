def incr(num,scale = 1):
    return num + scale

num = 2
res = incr(num)
print(res)
print(num)
# 输出3 2 可见py也是值传递，里面的修改不影响外面的值

print("*******************")
def loopPrintArr(nums):
    nums.remove(2)
nums = [1,2,3,4,5]
# loopPrintArr(nums)
# print(nums)

print("*******************")
loopPrintArr(nums[:])
print(nums)

# 函数中传入任意数量的形参
def printArr(*args):
    for arg in args:
        print(arg)
printArr(1,2,3,4,5)

print("*********************")
# 两个*是用来接受k-v的形式的，写法为k=v
def moreDes(topic,group,**users):
    print(topic,group,users)
moreDes("12","34",sd = "sad:sd",we = "34:df")
