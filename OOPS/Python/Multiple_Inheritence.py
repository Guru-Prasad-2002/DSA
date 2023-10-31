class Parent1:
    def method1(self):
        print("Parent class method 1")

class Parent2:
    def method2(self):
        print("Parent class method 2")

class Base(Parent1,Parent2):
    def method(self):
        print("Base class method")

Base_obj=Base()
Base_obj.method1()
Base_obj.method2()
Base_obj.method()