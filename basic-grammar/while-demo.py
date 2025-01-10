# count = 0
# while count < 5:
#     print(count)
#     count += 1

# input_message = input("Enter a message: ")
# while input_message != 'quit':
#     print(input_message)
#     input_message = input("Enter a message: ")

all_user = [
    {"name":"levi","isActive":True},
    {"name":"dyn","isActive":False},
    {"name":"jack","isActive":False},
    {"name":"jane","isActive":True},
]

confirm_user = []
un_confirm_user = []

while all_user:
    user = all_user.pop()
    if user["isActive"]:
        confirm_user.append(user)
    else:
        un_confirm_user.append(user)

for user in confirm_user:
    print(f"通过检查的人为{user.get('name').title()}")

for user in un_confirm_user:
    print(f"没有通过检查的人为{user.get('name').title()}")
