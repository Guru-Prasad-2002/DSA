class Parent:
    def random_function(self):
        print("This is Parent function")

    def random_function2(self):
        print("This is 2nd random function")

class Child(Parent):
    def random_function(self):
        print("This is Child function")

    def random_function2(self):
        super().random_function2()
        print("Utilized Random function of parent class in child class and now executing the remaining part of random function in child class")

Parent_obj=Parent()
Child_obj=Child()


# Parent_obj.random_function()
# Child_obj.random_function()


# Parent_obj.random_function2()
# Child_obj.random_function2()