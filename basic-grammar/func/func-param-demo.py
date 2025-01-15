def print_str(ele):
    return ele.strip()

clean_ops = [print_str, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
            result.append(value)
    return result

strs = [' 123 ','2','3','4']
res = clean_strings(strs, clean_ops)
print(res)