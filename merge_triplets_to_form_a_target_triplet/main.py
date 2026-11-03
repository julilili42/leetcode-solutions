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
METHOD = "mergeTriplets"


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        x, y, z = 0, 0, 0
        for i, [a, b, c] in enumerate(triplets):
            if not a > target[0] and not b > target[1] and not c > target[2]:
                x, y, z = max(a, x), max(b, y), max(c, z)

        return True if [x, y, z] == target else False


TESTS = [
    (([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]), True),
    (([[3, 4, 5], [4, 5, 6]], [3, 2, 5]), False),
    (([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]), False),
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
