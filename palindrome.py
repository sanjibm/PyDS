#!/usr/bin/env python

"""Problem Definition
Five Dwarves ( Gimli Fili Ilif Ilmig and Mark) met at the
Prancing Pony and played a word game to determine which
combinations of their names resulted in a palindrome.
Write a program in that prints out all of those combinations
"""

import itertools

def get_palindromes(names):
    """Generate a list of possible palindromes
    by using all permutations
    """
    perms = []
    results = []
    for length in range(2, len(names)):
        perms.extend(itertools.permutations(names, length))
    for p in perms:
        if check_palindrome1(''.join(p).lower()):
            results.append(p)
    return results

def check_palindrome1(str):
    """Check if single string is a palindrome or not
    Function uses two indices to compare extremeties
    of the input string
    """
    i = 0
    j = len(str) - 1

    while i <= j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

def check_palindrome2(str):
    return str == str[::-1]

if __name__ == '__main__':
    dwarves = ['Gimli', 'Fili', 'Ilif', 'Ilmig', 'Mark']
    print('Valid Palindromes found at the Prancing Pony...')
    print('\n'.join('{}'.format(item) for item in get_palindromes(dwarves)))
