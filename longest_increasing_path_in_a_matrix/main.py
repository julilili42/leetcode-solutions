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
METHOD = "longestIncreasingPath"


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        mem = {}

        def dfs(i: int, j: int, prev: int):
            if i < 0 or i == m or j < 0 or j == n:
                return 0
            if prev >= matrix[i][j]:
                return 0

            # prev not in key, since previous cell does not matter
            # when it comes to longest path. Only the condition that prev < curr
            key = (i, j)
            if key in mem:
                return mem[key]

            u = 1 + dfs(i + 1, j, matrix[i][j])
            d = 1 + dfs(i - 1, j, matrix[i][j])
            r = 1 + dfs(i, j + 1, matrix[i][j])
            l = 1 + dfs(i, j - 1, matrix[i][j])

            mem[key] = max(u, d, r, l)
            return mem[key]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, -1))

        return res


TESTS = [
    (([[9, 9, 4], [6, 6, 8], [2, 1, 1]],), 4),
    (([[3, 4, 5], [3, 2, 6], [2, 2, 1]],), 4),
    (([[1]],), 1),
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
