
#stack uses LIFO last in first out 
class Stack:
    
    #creating a constructor
    def __init__(self):
        self.items=[]
     
    #creating an empty stack   
    def is_empty(self):
        return self.items==[]

    def peek(self):
        return self.items[0]
    
    def get_size(self):
        return len(self.items)
    
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
s.push('D')
s.push('E')
s.pop()

print(s.print_stack())
print(s.is_empty())
print(s.peek())
print(s.get_size())