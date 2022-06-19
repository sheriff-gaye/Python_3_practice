
#creating a class
class Machine: 
    
    #creating a constructor 
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
        
    #creating a function    
    def talk(self):
        print(f"The {self.name}  cost {self.amount}")
        
#inherting from the main class     
class Item(Machine):
    
    #constructor
    def __init__(self,name,amount,color):
        self.name=name
        self.amount=amount
        self.color=color
        
    #function
    def desc(self):
        print(f"The Item is {self.name} and the color is {self.color} and it cost {self.amount}")
        
        
#object            
bike=Machine('Bicycle','5000')
print(bike.talk())

#object
bucket=Item('Bucket','400','Green')
print(bucket.desc())