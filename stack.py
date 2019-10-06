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

if __name__ == "__main__":
    #examples

    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')

    assert str(s) == 'cba'

    print(s)

    print('running pop...')
    s.pop()

    assert str(s) == 'ba'

    print(s)

    print('running pop...')
    s.pop()

    assert str(s) == 'a'

    print(s)


