#!/usr/bin/env python

"""
Wow, that was a tought one... to optimize
Took me a couple of iterations, but I've made it.
"""

import sys, itertools

def is_ugly(num):
    """Is it an ugly number?

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

def compute_number(signs, num):
    """Compute the number produced by interleaving signs with num
       For example, if signs = ['', '-', '+'] and num is 4673
       the computed number would be 46-7+3=42

        >>> get_number(['+', '-'], 143)
        2
        >>> get_number([''], 12)
        12
        >>> get_number(['+', '-', '', ''], 12345)
        -342
        >>> get_number(['', '-', '', '+'], 12345)
        -17
    """

    """

    Originally I use tring concatenation to construct operands,
    but then I realised that this could be optimzed by avoiding string operations
    alltogether

    # cnt = 0
    # operand = ""
    # val = 0
    # for i, c in enumerate(num[:-1]):
    #     operand += c
    #     if s[i]:
    #         val += int(operand)
    #         operand = s[i]
    # operand += num[-1]
    # val += int(operand)
    # return val

    """

    lnum = len(str(num))
    val = 0
    operand = 0
    multiplier = 1
    for i in reversed(range(lnum-1)):
        operand += num%10 * multiplier
        num /= 10
        if signs[i] == '+':
            multiplier = 1
            val += operand
        elif signs[i] == '-':
            multiplier = 1
            val -= operand
        else:
            multiplier*=10
            continue
        operand = 0
    val += (multiplier*num + operand)
    return val


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

    # compute a list of all the permutations of +, - and no sign
    for s in itertools.product(['+', '-', ''], repeat=len(num.lstrip())-1):
        """
        Originally I tried to construct strings an evaluate them afterwards
        but then I figured I could achieve better performance with
        evaluating operands one by one

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

        # l = ""
        # for d in range(len(num)-1):
        #     l += (num[d] + s[d])
        # l += num[-1]
        # # remove leading zeros in operands, as eval treats such numbers as octal
        # cnt += is_ugly(eval(re.sub(r'\b0+(?!\b)', '', l)))

        """

        cnt += is_ugly(compute_number(s,int(num)))

    return cnt

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f:
            print count_ugly_numbers(line.strip())
    sys.exit(0)