class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j 
        self.k=k 

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,ob):
        return Vector(self.i+ob.i,self.j+ob.j,self.k+ob.k)

v1=Vector(1,2,3)
v2=Vector(3,2,1)

print(v1+v2)
print(type(v1+v2))