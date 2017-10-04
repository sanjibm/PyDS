#!/usr/bin/env python

""" graph defintion using a set of tuples"""

from collections import defaultdict

class Edge(object):
    def __init__(self, vertex1, vertex2):
        self._vertex1 = vertex1
        self._vertex2 = vertex2

    def swap(self):
        return Edge(self._vertex2, self._vertex1)

    def __str__(self):
        return '(' + str(self._vertex1) + ',' + str(self._vertex2) + ')'

    def __eq__(self, other):
        return (self._vertex1 == other._vertex1)

    def __hash__(self):
        return (hash(self._vertex1) ^
                hash(self._vertex2))

class Node(object):
    def __init__(self, node):
        self._name = node

    @property
    def name(self):
        return self._name


    def __str__(self):
        return str(self._name)

    def __eq__(self, other):
        return (self._name == other._name)

    def __hash__(self):
        return (hash(self._name))

class Graph(object):
    def __init__(self, connections = None, directed = False):
        self._graph = set()
        self._directed = directed
        if connections is not None:
            self.add(connections)

    def setDirected(self, directed):
        self._directed = directed

    def add(self, connections):
        for k in connections:
            self.addEdge(k)


    def addEdge(self, edge):
        if self._directed:
            self._graph.add(edge)
        else:
            self._graph.add(edge)
            self._graph.add(edge.swap())

    def removeEdge(self, edge):
        if self._directed:
            self._graph.remove(edge)
        else:
            self._graph.remove(edge)
            self._graph.remove(edge.swap())

    def isConnected(self, node1, node2):
        if Edge(node1, node2) in self._graph:
            return True
        return False

    def findPath(self, node1):
        s = set()
        for k in self._graph:
            if self.isConnected(node1, k):
                s.add(k)
        return s


    def __str__(self):
        return ','.join(str(x) for x in self._graph)  #generator expression



if __name__ == "__main__":
    #driver code
    c = [Edge(Node(1), Node(2)), Edge(Node(2), Node(3)), Edge(Node(1), Node(3))]
    s = set(c)
    g = Graph()
    g.setDirected(True)
    g.add(s)
    print g
    g.addEdge(Edge(Node(3), Node(4)))
    print g
    g.removeEdge(Edge(Node(2), Node(3)))
    print g
    print g.isConnected(Node(4), Node(3))

    print g.findPath(Node(1))
