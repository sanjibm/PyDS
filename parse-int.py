# Converts a string to an integer

# What this method actually does is to check whether the input
# String is numeric or not, by the use of the regex \\d+,
# not proceeding in that case, and returning −1.
#
# In case it passes the check, it goes ahead, creates a char array
# out of the String, and for each character c, multiplies (c - 48)
# with 10 raised to the power its index to manage the place value system

import re


def parseInt(number):
    pattern = re.compile("\\d+")

    if not pattern.match(number):
        return -1

    sum = 0
    length = len(number)

    for i in range(length - 1, -1, -1):
        sum += (10 ** (length - i - 1)) * (ord(number[i]) - 48)

    return sum

print(parseInt('66'))
