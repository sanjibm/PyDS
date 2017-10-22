import timeit

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(alist):
   for i in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,i+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       alist[i], alist[positionOfMax] = alist[positionOfMax], alist[i]

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergeSort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a,b)

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quickSort(less)+equal+quickSort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print 'Length', len(arr)

#bubbleSort(arr)
#selectionSort(arr)
#print 'Sorted array is', mergesort(arr)
print 'Sorted array is',quickSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
