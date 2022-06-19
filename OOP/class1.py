

#creating a class in python
class Person:
    
    #creating a constructor
    def __init__(self,name):
        self.name=name
 
 #creating a function       
    def talk(self):
        print( f'hello { self.name} welcome to oop programming')

    def age(self):
        print( f'How old are you{self.name} ?')        

#creating an object
sheriff=Person('Sheriff Gaye')
sheriff.talk()   


#creating object 2
modou=Person('Modou Lamin Jobe') 
modou.talk()    