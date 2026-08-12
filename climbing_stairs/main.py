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
METHOD = "climbStairs"


class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(i: int):
            if i > n:
                return 0
            if i == n:
                return 1

            if i not in mem:
                mem[i] = dfs(i + 1) + dfs(i + 2)

            return mem[i]

        return dfs(0)


TESTS = [
    ((2,), 2),
    ((3,), 3),
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
