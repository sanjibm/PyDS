# Python3 Program for the binary
# representation of a given number
# https://www.youtube.com/watch?v=p0Vyq2_Q_uI&feature=youtu.be&t=149


def bin(n):
    if n > 1:
        bin(n // 2)  # perform a floor division

    print(n % 2, end="")  # make sure the putput stays on the same line


if __name__ == "__main__":
    bin(131)
    print()
    bin(4)