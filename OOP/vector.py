
#creating a class for vector calculation
class Vector:

    #constructor   
    def ___init__(self,x,y):
        self.x=x
        self.y=y
        
    #function
    def __add__(self,other):
        return Vector(self.x+ other.x,self.y+ other.y)
    
#objects
first=Vector(5,7)
second=Vector(1,3)
result=first+second
print(result.x)
        
    