
from linked_list import Node
from linked_list import LinkedList

class Stack(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def push(self, data):
        self.add(data)

    def pop(self):
        tmp = self.head.next
        x = self.head
        self.head = tmp
        return x

#examples

s = Stack()
s.push('a')
s.push('b')
s.push('c')

print s

print s.pop()
print s

print s.pop()
print s
