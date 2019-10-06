# Check if a String is composed of all unique characters
# OPTION 4: Array/list way
# Time: O(n)   Space: O(1) but influenced by the list of length 96
def unique_characters_list(input_string):
    if len(input_string)>96:  # 96 = number of printable chars
        return False
    chars_list = [False] * 96
    for char in input_string:
        # take list position by taking ascii position - 32 (amount of control characters)
        idx = ord(char)-32
        if chars_list[idx]:
            return False
        chars_list[idx] = True
    return True


# driver
str = 'abede'
print(unique_characters_list(str))
