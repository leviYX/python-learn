user = {
    "name":"levi",
    "age":18,
    "sex":"male"
}

def iteratorByKey(struct):
    for key in struct.keys():
        print(f"key is :{key}, value is :{struct[key]}")

def iteratorByValues(struct):
    for val in struct.values():
        print(f"value is :{val}")

def iterator(struct):
    for item in struct.items():
        print(f"the item is :{item}")

def setValueIfKeyNotExists(struct, key, value):
    struct.setdefault(key, value)

def setValueIfExists(struct, key, value):
    struct[key] = value

def checkkeyIfExists(struct, key):
    return key in struct.keys()


# setdefault()方法提供了一种方式，在一行中完成这件事。传递
# 给该方法的第一个参数，是要检查的键。第二个参数，是如果该键不
# 存在时要设置的值。如果该键确实存在，方法就会返回键的值,所以它不能用来修改一个key对应的value

user.setdefault("name","123")
print(user)

# 这样可以修改
user["name"] = "123"
print(user)

print(checkkeyIfExists(user, "name"))