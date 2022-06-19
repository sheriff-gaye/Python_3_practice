

class Animal:
    
    def __init__(self,name,color,legs):
        self.name=name
        self.color=color
        self.legs=legs
        
    def intro(self):
        print(f"My name is {self.name} and my color is {self.color} and has {self.legs} legs")
       

#creating an object 1
dog=Animal('Dog','Brown',4)
dog.intro()

#creating object 2
cat =Animal('Cat','White' ,4)
cat.intro()