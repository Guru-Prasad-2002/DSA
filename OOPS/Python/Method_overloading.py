class Overloading:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
    
obj=Overloading()
obj.add(2,3)
obj.add(2,3,4)