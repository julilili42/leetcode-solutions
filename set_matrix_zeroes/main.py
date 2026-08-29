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
METHOD = "setZeroesGood"


class Solution:
    # Time: O(m * n), Space: O(1)
    def setZeroesGood(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_col_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

    # Time: O(m * n), Space: O(m + n)
    def setZeroesNotThatBad(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        rows = [False] * m
        cols = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
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
    (([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    (
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],),
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    ),
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
