class Dog:
    def __init__(self, name, age):
        print(f"初始化创建dog{name},{age}")
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} eat {food}")
    def toString(self):
        print(f"self.name is {self.name}, self.age is {self.age}")

    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age