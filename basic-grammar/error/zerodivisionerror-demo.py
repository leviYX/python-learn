try:
    res = 100 / 0
except ZeroDivisionError:
    pass
    # print("除数不能为0")
else:
    print("123",res)