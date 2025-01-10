input_age = input("请输入你的年龄:")
print(f"ok,用户输入的年龄为{input_age}")

if int(input_age) >= 18: # input函数返回的是字符串，不能直接和数字比较，会强转异常，所以需要用int函数来转换
    print("ok")
else:
    print("no")

input_height = input("请输入你的身高")
input_height = int(input_height) # 也可以直接转，py不存在什么强类型
if input_height >= 100: print("ok")
else:print("no")