#!/usr/bin/env python

"""
Basic LinkList implementation using a ListNode class with related methods for
the node as well as for the list

Includes the additional functions on linked lists:
- merging two sorted lists
"""

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

def append(listHead, node):
    p = listHead
    while(True):
        if p.next != None:
            p = p.next
        else:
            p.next = node
            break
    return listHead



def createList(list):
    """
    create a linked list from a python listHead
    """
    n = ListNode()
    reference = None
    for i in reversed(list):
        tmp = ListNode(i, reference)
        reference = push(reference,tmp)
    return reference

def mergeTwoLists(l1, l2):
    """
    merge two sorted lists
    """
    if l1 == None and l2 != None:
        return l2
    elif l1 != None and l2 == None:
        return l1
    elif l1 == None and l2 == None:
            return None

    reference = ListNode(-1)
    prev = reference
    breakNextTime = False

    while (True):
        if breakNextTime:
            prev.next = extra
            break

        if l1.data <= l2.data:
            prev.next = l1
            l1 = l1.next
            if l1 == None:
                extra = l2
                breakNextTime = True

        else:
            prev.next = l2
            l2 = l2.next
            if l2 == None:
                extra = l1
                breakNextTime = True

        prev = prev.next

    return reference.next

def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None

    pa = headA # 2 pointers
    pb = headB

    while pa is not pb:
        # if either pointer hits the end, switch head and continue the second traversal,
        # if not hit the end, just move on to next
        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next

    return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None

if __name__ == "__main__":
    n1 = ListNode(5)
    n2 = ListNode(6)
    n3 = ListNode(9)

    #printList(n1)
    n1.setNext(n2)
    #printList(n1)

    n1 = push(n1, n3)
    #printList(n1)

    l1 = createList([1,2,4,6])
    l2 = createList([1,3,4])

    #s= mergeTwoLists(l1,l2)
    #printList(s)

    l3 = createList([8,9,10])
    l1 = append(l1,l3)
    l2 = append(l2,l3)

    #printList(l1)
    #printList(l2)

    s = getIntersectionNode(l1,l2)
    printList(s)
