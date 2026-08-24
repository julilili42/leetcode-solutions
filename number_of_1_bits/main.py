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
METHOD = "hammingWeight"


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n & (n - 1)
            res += 1

        return res

    def hammingWeightCount(self, n: int) -> int:
        return bin(n)[2:].count("1")

    def hammingWeightSlow(self, n: int) -> int:
        b = bin(n)[2:]
        total = 0
        for ch in b:
            total += int(ch)

        return total


TESTS = [
    ((11,), 3),
    ((128,), 1),
    ((2147483645,), 30),
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
