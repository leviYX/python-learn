def print_str(ele):
    return ele.strip()

clean_ops = [print_str, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
            result.append(value)
    return result

strs = [' 123 ','2','3','4']
res = clean_strings(strs, clean_ops)
print(res)

print("***********************")
def incr(num,scale):
    return num + scale
# lambda
def add2(nums,func):
    return [func(x) for x in nums]

res = add2([1,2,3,4,5],lambda x:incr(x,2))
print(res)