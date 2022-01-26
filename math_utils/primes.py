from math import floor, sqrt
def isprime(n):
    test = 0
    for a in range(2, floor(sqrt(n))+1):
        if n % a == 0:
            test += 1
    if test == 0:
        return True
    else:
        return False
