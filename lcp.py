
from itertools import takewhile,izip

x = ['rotyrt', 'rotydrfr','rotyund', 'rotywed', 'rotyst']


def allsame(x):
    print x
    print set(x)
    return len(set(x)) == 1

r = [i[0] for i in takewhile(allsame ,izip(*x))]

print ''.join(r)
