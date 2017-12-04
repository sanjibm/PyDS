"""
Fibonacci numbers using memoisation
"""

def fib(n):
    if n in fib.cache.keys():
        return fib.cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fib(n-2) + fib(n - 1)
    fib.cache[n] = result
    return result

if __name__ == "__main__":
    #initialize memo cache
    fib.cache = {}

    for i in range(100):
        print fib(i)
