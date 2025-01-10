def greet_user(prompt):
    print(f"Hello, user,the prompt is :{prompt}!")

def describe_pet(animal_type, pet_name = "defaultDog"):
    print(f"the animal type is : {animal_type}, the pet name is : {pet_name}")

greet_user("fuck python")

describe_pet(pet_name="python", animal_type="dog")
describe_pet(animal_type="dog")

# py的函数返回值，不需要声明，直接返回即可
def add_numbers(a, b):
    return a + b
res = add_numbers(1,2)
print(res)
