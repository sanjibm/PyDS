#!/usr/bin/env python

class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def getValue(self):
        return self.data

    def setValue(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

def printList(headNode):
        p = headNode
        while (True):
            print p.data
            if p.next == None:
                break
            p = p.next

def push(listHead, node):
    if node != None:
        node.next = listHead
    return node

def createList(list):
    n = ListNode()
    reference = None
    for i in reversed(list):
        tmp = ListNode(i, reference)
        reference = push(reference,tmp)
    return reference

def mergeTwoLists(p1, p2):
    reference = ListNode(-1)
    prev = reference
    while (True):

        if (p1.next == None) and (p2.next == None):
            print 'exiting...'
            print 'p1: ', p1.data, (p1.next)
            print 'p2: ', p2.data, (p2.next)
            break

        print 'p1: ', p1.data, (p1.next)
        print 'p2: ', p2.data, (p2.next)

        if p1.data <= p2.data:
            prev.next = p1
            p1 = p1.next
        else:
            prev.next = p2
            p2 = p2.next


        prev = prev.next


    return reference



if __name__ == "__main__":
    n1 = ListNode(5)
    n2 = ListNode(6)
    n3 = ListNode(9)

    #printList(n1)
    n1.setNext(n2)
    #printList(n1)

    n1 = push(n1, n3)
    #printList(n1)

    l1 = createList([1,2,4])
    l2 = createList([1,3,4])

    s= mergeTwoLists(l1,l2)
    printList(s)
