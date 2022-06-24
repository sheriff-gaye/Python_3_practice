
#queue uses FIFO

class Queue:

    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        return self.items[0]
    
    def get_size(self):
        return len(self.items)
    
    def queue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def print_queue(self):
        return self.items

s=Queue()
s.queue(1)
s.queue(2)
s.queue(3)
s.queue(4)
s.queue(5)
s.dequeue()


print(s.print_queue())
print(s.is_empty())
print(s.peek())
    
    