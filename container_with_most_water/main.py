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
METHOD = "maxArea"


class Solution:
    def maxAreaBruteForce(self, height: List[int]) -> int:
        max_area = 0

        for i in range(len(height)):
            l = height[i]
            for j in range(i + 1, len(height)):
                r = height[j] 
                print(f"{min(l,r)} * {j - i} = {min(l, r) * (j-i)}")
                max_area = max(max_area, min(l, r) * (j - i))

        return max_area
    

    # since hanging on to the smaller pillar can not yield us a higher area
    # we always move the smaller one.
    #
    # Proof:
    # Assume height[l_1] > height[r_1], then we have
    # area_1 = min(height[l_1], height[r_1]) * (r_1 - l_1)
    # Distance d_2 < d_1 = (r_1 - l_1) decreases with each iteration no matter what, we have to
    # move a pointer. 
    # Therefore min(height[l], height[r]) of iteration 2 must be larger then the previous iteration
    # s.t. area_2 > area_1
    # but this can only be the case if a larger height then the previous iteration is achieved
    
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            # discard lower height
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area
                



TESTS = [
    (([1,8,6,2,5,4,8,3,7],), 49),
    (([1,1],), 1),
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
