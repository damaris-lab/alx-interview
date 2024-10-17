#!/usr/bin/python3
def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
if __name__ == "__main__":
    print(minOperations(9))
    print(minOperations(12))
