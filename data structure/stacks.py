
#stack uses LIFO last in first out 
#the last that came into the list will go out first 
#learning about stack data structure
class Stack:
    
    #creating a constructor
    def __init__(self):
        self.items=[]
     
    #creating an empty stack   
    def is_empty(self):
        return self.items==[]
    
    #pushing/adding items to the stack
    def push(self,item):
        self.items.insert(0,item)
     
    #removing items from the stack   
    def pop(self):
        return self.items.pop(0)
    
    #print stack
    def print_stack(self):
        print(self.items)
        
#creating objects
s=Stack()
s.push('A')
s.push('B')
s.push('C')
s.pop()

print(s.print_stack())