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
METHOD = "tribonacci"


class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {}

        def rec(n: int):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1

            nonlocal mem
            if n in mem:
                return mem[n]

            mem[n] = rec(n - 3) + rec(n - 2) + rec(n - 1)

            return mem[n]

        return rec(n)


TESTS = [
    ((4,), 4),
    ((25,), 1389537),
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
