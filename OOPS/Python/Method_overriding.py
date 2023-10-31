class Parent:
    def fun(self):
        print("This is parent function that will get overridden")

class Child(Parent):
    def fun(self):
        print("This is the child function that is overriding parent function")
    
ob=Child()
ob.fun()