
#creating a class
class Animal:
    
    #creating a constructor
    def __init__(self,name,color,legs):
        self.name=name
        self.color=color
        self.legs=legs
  
  #creating a class function  
    def intro(self):
        print(f"I am an Animal my name is {self.name} my color is {self.color} and i have {self.legs} legs")
  
#dog class inherting from animal class
class Dog(Animal):
    
    #creating a dog  function
    def bark(self):
        print('wooof , woof , woof')      
        
#creating a cat class
class Cat(Animal):
    
    #creating a cat function
    def meew(self):
        print("hello i am a cat")  
        
            
#creating an object
dog=Dog('Dog','Brown','4')
dog.intro()
dog.bark()
        
        