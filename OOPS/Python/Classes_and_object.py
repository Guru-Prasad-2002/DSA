class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name={self.name},Age={self.age}"

dog_object=Dog("John",5)
print(dog_object)