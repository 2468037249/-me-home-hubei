class Dog():
    def __init__(self, name):
        self.name = name
        self.__age = 70

    def getName(self):
        return self.name

    def gatAge(self):
        return self.__age

dog = Dog('二哈')
print(dog.getName())
print(dog.gatAge())
