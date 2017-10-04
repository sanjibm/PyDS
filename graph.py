#!/usr/bin/env python

""" graph defintion using a set of dicts"""

from collections import defaultdict

class Edge(object):
    def __init__(self, node1, node2):
        self.__vertex1 = node1
        self.__vertex2 = node2
        self.tuple = tuple((node1, node2))

class Graph(object):
    def __init__(self, connections = None, directed = False):
        self._graph = defaultdict(set)
        self._directed = directed
        if connections is not None:
            self.add(connections)
        else:
            self._graph = set()

    def setDirected(self, directed):
        self._directed = directed

    def add(self, connections):
        for k in connections:
            self.addNode(k[0], k[1])


    def addNode(self, node1, node2):
        if self._directed:
            t = tuple((node1, node2))
            self._graph.add(t)
        else:
            t1 = tuple((node1, node2))
            t2 = tuple((node2, node1))
            self._graph.add(t1)
            self._graph.add(t2)

    def removeNode(self, node):
        if self._directed:
            self._graph.remove(node)
        else:
            self._graph.remove(node)
            self._graph.remove(tuple((node[1], node[0])))

    def isConnected(self, node1, node2):
        if tuple((node1, node2)) in self._graph:
            return True
        return False

    def findPath(self, node1, node2):
        s = set()
        for k in self._graph:
            if isConnected(node1, k):
                s.add(k)
        return s


    def __str__(self):
        return str(self._graph)


c = [(1,2),(2,3),(1,3)]
s = set(c)
g = Graph()
g.setDirected(True)
g.add(s)
g.addNode(3,4)
print g

#g.removeNode((5,6))
#print g

print g.isConnected(1,2)

print findPath()
