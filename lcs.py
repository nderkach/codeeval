#!/usr/bin/python

import sys
import unittest


def lcs_helper(s1, s2):
    m, n = len(s1), len(s2)
    C = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return (C, int(C[m][n]))


def backtrack(C, s1, s2, i, j):
    if (i == 0 or j == 0):
        return ""
    elif s1[i-1] == s2[j-1]:
        return backtrack(C, s1, s2, i-1, j-1) + s1[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return backtrack(C, s1, s2, i, j-1)
        else:
            return backtrack(C, s1, s2, i-1, j)


def lcs_dynamic(string):
    s1, s2 = string.split(';')
    assert(0 < (len(s1) or len(s2)) < 50)
    C = lcs_helper(s1, s2)[0]
    return backtrack(C, s1, s2, len(s1), len(s2))


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(lcs_helper("XMJYAUZ", "MZJAWXU")[1], 4)
        self.assertEqual(lcs_helper("GAC", "AGCAT")[1], 2)
        self.assertEqual(lcs_dynamic("GAC;AGCAT"), "GA")
        self.assertEqual(lcs_dynamic("AGCAMT;GACRM"), "ACM")
        self.assertEqual(lcs_dynamic("ABCDEFG;BCDGK"), "BCDG")

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        unittest.main()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if line.strip():
                res = lcs_dynamic(line.strip())
                print(res)
