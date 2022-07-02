

class Node:

    def __init__(self,data,next):
        self.data=data
        self.next=next


class linkedList:

    def __init__(self):
        self.head=None


    def add_top(self,data):
        self.head=Node(data,self.head)


    def add_bottom(self,data):
        if not self.head:
            self.head=Node(data,None)
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=Node(data,None)



    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()



    def is_empty(self):
        return self.head==None



helo=linkedList()
helo.add_top(1)
helo.add_bottom(5)
helo.add_top(2)
helo.print_list()
print(helo.is_empty())