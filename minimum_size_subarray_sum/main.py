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
METHOD = "minSubArrayLen"


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        l = 0
        total = 0
        n = len(nums)
        min_length = n + 1

        for r in range(n):
            total += nums[r]

            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if min_length == n + 1 else min_length


TESTS = [
    ((7, [2, 3, 1, 2, 4, 3]), 2),
    ((4, [1, 4, 4]), 1),
    ((11, [1, 1, 1, 1, 1, 1, 1, 1]), 0),
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
