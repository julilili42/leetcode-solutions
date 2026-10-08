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
METHOD = "myPow"


class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)

        def recursion(n):
            if n == 0:
                return 1

            half = recursion(n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        ans = recursion(N)
        return 1 / ans if n < 0 else ans


TESTS = [
    ((2.0, 10), 1024.0),
    ((2.1, 3), 9.26100),
    ((2.0, -2), 0.25),
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
