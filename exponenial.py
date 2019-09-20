# modified pow function that raises a to the power of b
# without using multiplication or division
def modPow(a, n):
    # convert a to positive number
    answer = abs(a)

    # store exponent for later use
    exp = n

    # loop n times
    while n > 1:

        # add the previous added number n times
        added = 0
        for i in range(0, abs(a)):
            added += answer
        answer = added
        n -= 1

    # if a was negative determine if the answer will be
    # positive or negative based on the original exponent
    # e.g. pow(-4, 3) = (-4)^3 = -64
    if a < 0 and exp % 2 == 1:
        return -answer
    else:
        return answer


print
print(modPow(2, 10))
# print modPow(5, 4);
# print modPow(-4, 7);