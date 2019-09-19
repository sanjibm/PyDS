# Determine if 2 Strings are anagrams


from functools import reduce
a = 'abcdefghijklmnopqrstuvwxyz'
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
     71, 73, 79, 83, 89, 97, 101]
d = dict(zip(a, p))

def prod(s):
        return reduce((lambda n1, n2: n1*n2), [d[lett] for lett in s])

def is_anagram(s1, s2):
        return prod(s1) == prod(s2)

# driver

u = 'lives'
v = 'svile'
print(is_anagram(u, v))