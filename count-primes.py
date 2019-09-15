# Sift the Two's and Sift the Three's,
# The Sieve of Eratosthenes.
# When the multiples sublime,
# The numbers that remain are Prime.


def countPrimes(n):

    if n == 0:
        return 0
    sieve = (n)*[True]
    sieve[0] = False
    if n >= 2:
        sieve[1] = False

    for num in range(2, len(sieve)):
        for e in range(num + 1, len(sieve)):
            if e % num == 0:
                sieve[e] = False

    for i, x in enumerate(sieve):
        print(i, x)

    count = 0
    for x in sieve:
        if x:
            count += 1

    return count

print(countPrimes(20))
