#!/usr/bin/env python
import sys, itertools, re

def is_ugly(num):
    """Is it an ugly number

        >>> is_ugly(14)
        True
        >>> is_ugly(13)
        False
        >>> is_ugly(39)
        True
        >>> is_ugly(121)
        False
        >>> is_ugly(0)
        True
    """

    return any([not num%i for i in [2, 3, 5, 7]])

def count_ugly_numbers(num):
    """Counts the number of ugly numbers which could be derived from num

        >>> count_ugly_numbers('1')
        0
        >>> count_ugly_numbers('9')
        1
        >>> count_ugly_numbers('011')
        6
        >>> count_ugly_numbers('12345')
        64
    """

    cnt = 0

    # get the list of permutations of '+', '-' and ''(no sign) signs
    sign_list = [sign_permutation for sign_permutation in itertools.product(['+', '-', ''], repeat=len(num)-1)]

    """
       interleave the number with all the sign permutations
       3**(D-1) permutations, where D is the number of digits in num
       i.e. if num = 123
       the outer loop will produce string like:
       123
       1+2+3
       12+3
       1+23
       1+2-3
       1-2+3
       1-2-3
       1-23
       12-3
    """
    for s in [list(tup) for tup in sign_list]:
        l = ""
        for d in range(len(num)-1):
            l += (num[d] + s[d])
        l += num[-1]
        # remove leading zeros in operands, as eval treats such numbers as octal
        cnt += is_ugly(eval(re.sub(r'\b0+(?!\b)', '', l)))

    return cnt

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f:
            print count_ugly_numbers(line.strip())
    sys.exit(0)
