
# checks whether xth bit is set in a mask
def isBitSet(mask, x):
    return (mask >> x) & 1
# mask = 1010
# isBitSet(1) -> (1010 >> 1) & 1 = 0101 & 0001 = 1 (is set)

# sets xth bit in a mask


def setBit(mask, x):
    return mask | (1 << x)
# mask = 1010
# setBit(2) -> 1010 | (1<<2) = 1010 | 0100 = 1110


# flips xth bit in a mask
def flipBit(mask, x):
    return mask ^ (1 << x)
# mask = 1010
# flipBit(1) -> 1010 ^ (1<<1) = 1010 ^ 0010 = 1000


def clearBit(mask, x):
    return mask & ~(1 << x)
# mask = 1010
# clearBit(1) -> 1010 & ~(1<<1) = 1010 & ~0010 = 1010 & 1101 = 1000


# checks if number is even
def isEven(mask):
    return mask & 1 == 0


# checks if number is odd
def isOdd(mask):
    return mask & 1 == 1


# checks if number is divisible by 2^k
def isDivisibleByPowerOfTwo(n, k):
    powerOfTwo = 1 << k
    return n & (powerOfTwo-1) == 0


# checks if a number is a power of two
def isPowerOfTwo(n):
    return n and n & (n-1) == 0


# clears the right-most set bit
def clearRightmostSetBit(mask):
    return mask & (mask-1)


# Brian Kernighan's algorithm
# counting the number of bits by clearing the right-most set bit one by one
def countSetBits(n):
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count
