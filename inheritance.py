
#creating a class
class Animals:
    #ceating method of the class
    def walk(self):
        print('Talk')
  
#sub classes inherting from main class      
class Dog(Animals):
    def bark(self):
        print('hello i am a dog 🐕‍🦺🦮')
        
class Cat(Animals):
    def meew(self):
        print('hello i am cat 🐱🐺')
        
        
#creating objects 1
dog1= Dog()
print(dog1.bark())


#creating oobject 2
cat=Cat()
print(cat.meew())
        

    