
#learning about queue in python

#queue class

class Queue:
    
    #queue constructor
    def __init__(self):
        self.items=[]
        
    #creating an empty queue
    def is_empty(self):
        return self.items==[]
    
    #queueing function
    def queue(self,item):
        self.items.insert(0,item)
        
    #dequeueing function
    
    def dequeue(self):
        return self.items.pop()
    
    #print queue
    def print_queue(self):
        print(self.items)

#creating objects
q=Queue()
q.queue(1)
q.queue(2)
q.queue(3)
q.dequeue()

print(q.print_queue())

        
        
    
    