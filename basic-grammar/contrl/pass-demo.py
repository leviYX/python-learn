# pass 跳过当前代码，什么都不执行
nums = ['one', 'two', 'three',None,'four',None]

for item in nums:
    if item is None:
        # do nothing ,use pass skip this code block
        pass
    else:
        print(item)