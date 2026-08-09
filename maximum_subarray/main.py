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
METHOD = "maxSubArray"


class Solution:
    # Kadane's Algorithm
    # O(n), O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        total = 0
        for i in range(len(nums)):
            if total < 0:
                total = nums[i]
            else:
                total += nums[i]
            res = max(res, total)

        return res

    # O(n^2), O(1)
    def maxSubArraySlow(self, nums: List[int]) -> int:
        res = float("-inf")

        # at each index start a new summation of the next subsequence (i to end)
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                res = max(res, total)

        return res


TESTS = [
    (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
    (([5, 4, -1, 7, 8],), 23),
    (([1],), 1),
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
