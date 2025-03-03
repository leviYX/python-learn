import random

def func1():
    seed = random.randint(1,10)
    print("这里有一个随机数，位于1-10之间，你有8次机会猜到这个数字是多少。")
    guess = 100
    for i in range(8):
        guess = int(input())
        if guess == seed:
            print(f"恭喜你猜对了，你只猜了{i} 次")
            break
        if guess > seed:
            print("对不起，你猜测的有点大了...")
        if guess < seed:
            print("对不起，你猜测的有点小了...")

def func2():
    arr = ["levi","tom","jerry","jack"]
    for i in range(len(arr)):
        print(arr[i])

def checkItem(item,arr):
    return item in arr
# res = checkItem("levi",["levi","tom","jerry"])
# print(res)

name,age,sex = ["tom",12,"man"]
print(f"{age}")

names = ("levi","tom","jerry","jack")
print(type(names))