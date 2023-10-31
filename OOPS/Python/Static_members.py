class Random_class:
    static_var=0

    def non_static_function(self):
        print("This is a non static function")
    
    @staticmethod
    def static_method():
        print("This is a static method in python")

ob=Random_class()

# ob.non_static_function()
# ob.static_method() #error

# Random_class.static_method()
print(ob.static_var)
print(Random_class.static_var)
