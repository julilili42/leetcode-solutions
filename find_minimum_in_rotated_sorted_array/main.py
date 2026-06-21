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
METHOD = "findMin"


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]


    def findMinStandard(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_element = float("inf")

        while l <= r:
            m = l + (r - l) // 2
            
            # left side is sorted
            if nums[m] >= nums[l]:
                min_element = min(min_element, nums[l])
                l = m + 1
            
            # right side is sorted
            if nums[m] < nums[r]:
                min_element = min(min_element, nums[m])
                r = m - 1
        
        return min_element





TESTS = [
    (([3,4,5,1,2],), 1),
    (([4,5,6,7,0,1,2],), 0),
    (([11,13,15,17],), 11),
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
