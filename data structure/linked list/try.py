
class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def add_at_top(self, data):
        self.head = Node(data, self.head)

    def add_at_bottom(self,data):
        if not self.head:
            self.head = Node(data, None)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, None)

    def is_empty(self):
        return self.head == None

    def get_last_node(self):
        n=self.head
        while n.next!=None:
            n=n.next
        return n.data

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end=" => ")
            n = n.next
        print()


class4=LinkedList()
class4.add_at_top('sheriff')
class4.add_at_top('gaye')
class4.add_at_bottom('jobiz')
class4.print_list()
print(class4.get_last_node())