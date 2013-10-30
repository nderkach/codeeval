#!/usr/bin/env python
import sys, itertools

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

def count_ugly(num):
    """Counts the number of ugly numbers which could be derived from num

    """

    cnt = 0
    # # start by checking the number itself
    # cnt = int(is_ugly(num))
    snum = num

    sign_list = [c for c in itertools.product(['+', '-', ''], repeat=len(snum)-1)]

    for s in [list(t) for t in sign_list]:
        l = ""
        for d in range(len(snum)-1):
            l+=(snum[d] + s[d])
        l+=snum[-1]
        # print s
        # print l
        # print eval(l.lstrip('0'))
        cnt += is_ugly(eval(l.lstrip('0')))

    return cnt

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f:
            print line.strip()
            print count_ugly(line.strip())
            print '------'