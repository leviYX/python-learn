# 关于map的嵌套使用

# 可以用集合数组来存储多个map
user_0 = {"name":"levi","age":18,"sex":"male"}
user_1 = {"name":"dyn","age":20,"sex":"female"}

# users = [user_0,user_1]
# for user in users:
#     print(user)

# test
# aliens_list = []
# for i in range(10):
#     if i % 2 == 0:
#         aliens = {"name": "levi", "age": i, "sex": "male"}
#         aliens_list.append(aliens)
#     else:
#         aliens = {"name": "dyn", "age": i, "sex": "female"}
#         aliens_list.append(aliens)
# # 显示前5个外星人。
# for aliens in aliens_list[0:5]:
#     print(aliens)
#
# print(f"aliens_list 中一共{len(aliens_list)}个外星人")

# test:在字典中存储列表
mate_class = {
    "teacher":"mr cat",
    "student":[{"name":"levi","age":18},{"name":"dyn","age":20}]
}
for student in mate_class["student"]:
    print(student)
