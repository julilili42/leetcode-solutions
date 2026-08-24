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
METHOD = "solve"


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}

        def dfs(i: int, j: int):
            if i == m - 1 and j == n - 1:
                return 1
            if i == m or j == n:
                return 0

            key = (i, j)
            if key in mem:
                return mem[key]

            d = dfs(i + 1, j)
            r = dfs(i, j + 1)

            mem[key] = d + r
            return mem[key]

        return dfs(0, 0)


TESTS = [
    (
        (
            3,
            7,
        ),
        28,
    ),
    (
        (
            3,
            2,
        ),
        3,
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
