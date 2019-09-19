# Python code to reverse a string
# using loop & recursion

def reverse1(s):
    str = ""
    for i in s:
        str = i + str
    return str

def reverse2(s):
    if len(s) == 0:
        return s
    else:
        return reverse2(s[1:]) + s[0]


s = "Duh"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse1(s))

print("The reversed string(using recursion) is : ", end="")
print(reverse2(s))