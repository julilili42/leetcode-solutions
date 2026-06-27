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
METHOD = "search"


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            # left side is sorted
            # need to allow equality since it is possible that: l = m
            if nums[m] >= nums[l]:
                # check if target in [nums[l], nums[m])
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right side is sorted
            else:
                # check if target in (nums[m], nums[r]]
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1 
        
        return -1

TESTS = [
    (([4,5,6,7,0,1,2], 0,), 4),
    (([4,5,6,7,0,1,2], 3,), -1),
    (([5,6,1,2,3,4], 6,), 1),
    (([5,6,7,1,2,3,4], 2,), 4),
    (([3,5,1], 3,), 0)
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
