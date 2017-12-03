from itertools import takewhile,izip

s = '[{c%2}/{(a)}*(b+1)]'

def isValid(s):

    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
    return len(stack) == 0

print isValid(s)
