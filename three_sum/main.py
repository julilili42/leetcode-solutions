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
METHOD = "threeSum"


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        # Since we have three pointers and j < l < r must be statisfied, 
        # we only iterate to index j < len(nums) - 2. 
        for j in range(len(nums) - 2):
            l = j + 1
            r = len(nums) - 1 
            
            # Since the nums is sorted we know that
            # nums[j] < nums[l] < nums[r]
            # if nums[j] > 0 we get
            # 0 < nums[l] < nums[l] 
            # therefore total > 0 and we break 
            if nums[j] > 0:
                break


            # Since nums is sorted and j is fixed and j < l < r,
            # we can skip a nums[j] if we already checked it.
            if j > 0 and nums[j] == nums[j - 1]:
                continue

            while l < r:
                total = nums[j] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Similar logic as before, we can skip values which we already
                    # checked. 
                    # Since we move l and r inside, we have to make sure that 
                    # l < r is still correct. 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # nums[r + 1] is no problem since r -= 1 beforehand
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1 

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return result
                



TESTS = [
    (([-1,0,1,2,-1,-4],), [[-1,-1,2],[-1,0,1]]),
    (([0,1,1],), []),
    (([0,0,0],), [[0,0,0]]),
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
