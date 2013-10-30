#!/usr/bin/env python
import sys

"""
I've done some tests with timeit and it seems that both numeric and string version
have the same performance (at least for numbers < 10000)

# def reverse_num(num):
#   rev = 0
#   while(num > 0):
#     rev = (10*rev)+num%10
#     num //= 10
#   return rev
"""

def reverse(num):
    """Reverses the number

       >>> reverse(1456)
       6541
       >>> reverse(111)
       111
    """
    return int(str(num)[::-1])

def palindrome(num):
    """Return the number of iterations required to compute a palindrome

       >>> palindrome(195)
       (4, 9339)
    """
    # compute in 100 iterations or less
    for i in range(100):
        rnum = reverse(num)
        if rnum == num:
            break
        num = num + rnum
    return (i, num)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f:
            print "%s %s" % palindrome(int(line))
