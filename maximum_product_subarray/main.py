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
METHOD = "maxProduct"


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        cur_max, cur_min, res = nums[0], nums[0], nums[0]

        for i in range(1, n):
            old_max = cur_max
            old_min = cur_min
            cur_max = max(nums[i], old_max * nums[i], old_min * nums[i])
            cur_min = min(nums[i], old_min * nums[i], old_max * nums[i])

            res = max(res, cur_max)

        return res


TESTS = [
    (([2, 3, -2, 4]), 6),
    (([-2, 0, -1]), 0),
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
