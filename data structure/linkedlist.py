
#creating a node class

class Node:
    
    #constrctor
    def __init__(self,data,next):
        self.data=data
        self.next=next
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def add_at_front(self,data):
        self.head=Node(data,self.head)
        
    def add_at_end(self,data):
        if not self.head:
            self.head=Node(data,None)
            return 
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(data,None)
            