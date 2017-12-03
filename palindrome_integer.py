'''
For number 1221, if we do 1221 % 10, we get the last digit 1, to get the second
to the last digit, we need to remove the last digit from 1221, we could do so by
dividing it by 10, 1221 / 10 = 122. Then we can get the last digit again by doing
a modulus by 10, 122 % 10 = 2, and if we multiply the last digit by 10 and add
the second last digit, 1 * 10 + 2 = 12, it gives us the reverted number we want.
Continuing this process would give us the reverted number with more digits.
Now the question is, how do we know that we've reached the half of the number?
Since we divided the number by 10, and multiplied the reversed number by 10, when
the original number is less than the reversed number, it means we've processed
half of the number digits.
'''

def is_palindrome(a):
    if a < 0 or (a % 10 == 0 and a <> 0):
        return False
    if a == 0:
        return True

    invertedNumber = 0

    #When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    #For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    #since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.

    while (a > invertedNumber):
        invertedNumber = invertedNumber * 10 + a % 10
        a = a/10

    print invertedNumber, a
    return a == invertedNumber or a == invertedNumber/10


print is_palindrome(10)
print is_palindrome(121)
print is_palindrome(12763)
print is_palindrome(1221)
print is_palindrome(456654)
