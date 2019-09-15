
# Iterative Binary Search Function
# It returns location of x in given array arr if present,
# else returns None

arr = [56,45,23,5,2,76,45,12,16,78,9,14,28,52,95]
arr.sort()

toSearch = int(input('Enter a number: '))


def binarySearch(s, a):
    start = 0
    end = len(a) - 1
    for i in range(start, end):
        mid = int((start + end)/2)

        if s == a[mid]:
            return mid
        if s < a[mid]:
            end = mid - 1
            continue
        if s > a[mid]:
            start = mid + 1
            continue

print(arr)
print(binarySearch(toSearch, arr))
