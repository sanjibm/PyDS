class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __init__(self, firstnode):
        self.head = firstnode

    def add(self, element):
        node = Node(element)

        node.next = self.head
        self.head = node

    def search(self, element):
        pointer = self.head

        while True:
            if pointer.data == element:
                return pointer
            pointer = pointer.next

    def size(self):
        length = 0
        pointer = self.head
        while True:
            if pointer == None:
                return length
            pointer = pointer.next
            length += 1

    def show(self):
        pointer = self.head
        while True:
            print('->' + str(pointer.data), end = '')
            if pointer.next == None:
                break
            pointer = pointer.next







# driver


n1 = Node(5)


ll = LinkedList(n1)
ll.add(4)
ll.add(9)
ll.show()
print()

print(ll.size())
print()
ll.show()
print()

print(ll.size())

print(ll.search(4).data)





