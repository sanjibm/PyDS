from collections import OrderedDict  # dict subclass that remembers the order entries were added


class LRUCache:

    def __init__(self, capacity: int):
        self.cacheLine = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cacheLine:
            value = self.cacheLine[key]
            del self.cacheLine[key]  # removing from list
            self.cacheLine[key] = value  # adding again to make it most recent
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.cacheLine:
            del self.cacheLine[key]
        else:
            if len(self.cacheLine) == self.capacity:
                self.cacheLine.popitem(last=False)  # remove the first item
        self.cacheLine[key] = value


#driver
myCache = LRUCache(3)

myCache.put(1, 'One')
myCache.put(2, 'Two')
myCache.put(3, 'Three')
myCache.put(1, 'One')
myCache.put(4, 'Four')

print(myCache.get(1))

