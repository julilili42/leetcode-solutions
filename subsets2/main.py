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
METHOD = "subsetsWithDup"


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # duplicates are in sequence
        nums = sorted(nums)
        res = []
        subset = []

        def dfs(i: int):
            if i == len(nums):
                res.append(subset.copy())
                return
            # add number to subset
            subset.append(nums[i])
            dfs(i + 1)

            # do not add number to subset
            subset.pop()
            # if we do not take number we skip all numbers which are equal to skipped number
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            dfs(j)

        dfs(0)
        return res


TESTS = [
    (([1, 2, 2],), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    (([0],), [[], [0]]),
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
