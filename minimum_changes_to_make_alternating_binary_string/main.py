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
METHOD = "minOperations"


class Solution:
    def minOperations(self, s: str) -> int:
        j = 0
        n = len(s)
        changes = 0

        for ch in s:
            j ^= 1
            if int(ch) == j:
                changes += 1

        return min(changes, n - changes)


TESTS = [
    (("0100",), 1),
    (("10",), 0),
    (("1111",), 2),
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
