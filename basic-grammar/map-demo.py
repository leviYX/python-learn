favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'levi': 'java',
 'phil': 'python',
}

# set函数做去重
for value in set(favorite_languages.values()):
    print(value)

print("****************")
# 遍历map的所有value
for value in favorite_languages.values():
    print(value)


levi_language = favorite_languages['levi'].title()
print(f"levi favorite language is {levi_language}")

# get可以避免当key在map中不存在的时候指定一个默认值，否则就会报错
# dyn_language = favorite_languages['dyn'].title()
# print(f"dyn favorite language is {dyn_language}")
dyn_language = favorite_languages.get("dyn","default value when the key is not exist")
print(f"dyn favorite language is {dyn_language}")

# test1,使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name 、last_name 、age 和city 。将存储在该字典中的每项信息都打印出来。
like_person = {}
like_person["first_name"] = "John"
like_person["last_name"] = "Smith"
like_person["age"] = "18"
like_person["city"] = "London"
print(like_person)

# test2，　使用一个字典来存储一些人喜欢的数。请想出5个人的名字，并将这些名字用作字典中的键；找出每个人喜欢的一个数，并将这些数作为值存储在字典中。
# 打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。
like_number = {}
like_number["levi"] = 66
like_number["dyn"] = 77
print(like_number)

# test3,遍历map中的所有k-v
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nkey is :{key}")
    print(f"value is :{value}")

# test4、遍历map中的所有k,当我们不需要处理value的时候就可以用keys()函数来只取出key
for key in user_0.keys():
    print(f"\nkey is :{key}")
# test5、对key进行排序之后的遍历
for language_key in sorted(favorite_languages.keys()):
    language = favorite_languages[language_key]
    if language == "python":
        print(f"the key is :{language_key}")