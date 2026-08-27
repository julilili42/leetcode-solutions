from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from math import inf, gcd
import sys


# Change this to the LeetCode method name
METHOD = "setZeroes"


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        zeroes_row = [False] * m
        zeroes_col = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes_row[i] = True
                    zeroes_col[j] = True

        for i in range(m):
            for j in range(n):
                if zeroes_row[i] or zeroes_col[j]:
                    matrix[i][j] = 0

    def setZeroesBad(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        zeros = defaultdict(list)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros[i].append(j)

        def multiply_zero(matrix: List[List[int]], zeros):
            for row, cols in zeros.items():
                for col in cols:
                    for r in range(m):
                        matrix[r][col] = 0

                matrix[row] = [0] * n

        multiply_zero(matrix, zeros)


TESTS = [
    # Format:
    # ((arg1, arg2, ...), expected),
    # Example:
    # (([2, 7, 11, 15], 9), [0, 1]),
]


def run_tests():
    solution = Solution()
    fn = getattr(solution, METHOD)

    if not TESTS:
        print("No tests yet.")
        return

    for i, (args, expected) in enumerate(TESTS, 1):
        got = fn(*args)

        if got == expected:
            print(f"Test {i}: OK")
        else:
            print(f"Test {i}: FAIL")
            print(f"  got:      {got}")
            print(f"  expected: {expected}")


if __name__ == "__main__":
    run_tests()
