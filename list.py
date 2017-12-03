#!/usr/bin/env python

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def getValue(self):
        return self.data


if __name__ == "__main__":
    n1 = Node(5)
    print n1.getValue()
