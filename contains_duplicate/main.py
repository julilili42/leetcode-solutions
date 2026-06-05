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
METHOD = "containsDuplicateOptimized"


class Solution:
    def containsDuplicateBruteforce(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        
        previous = 0
        for i in range(1, len(nums)):
            if nums[previous] == nums[i]:
                return True
            previous = i
        
        return False
    

    def containsDuplicateOptimized(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

TESTS = [
    (([1,2,3,1],), True),
    (([1,2,3,4],), False),
    (([1,1,1,3,3,4,3,2,4,2],), True),
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
