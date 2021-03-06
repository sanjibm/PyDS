# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.

import collections


def firstUniqChar(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    # build hash map : character and how often it appears
    count = collections.Counter(s)

    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1

# driver
str = 'abracadabra'
print(firstUniqChar(str))