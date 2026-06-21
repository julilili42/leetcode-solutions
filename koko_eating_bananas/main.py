from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import math
import sys


# Change this to the LeetCode method name
METHOD = "minEatingSpeed"


class Solution:
    # binary search template: 
    # https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultima-sx6q/
    
    # binary search over solution space
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed: int) -> bool:
            # calculate time per pile given a constant speed
            time_per_pile = [math.ceil(pile / speed) for pile in piles]
            return sum(time_per_pile) <= h
        
        # lower speed bound: 1 banana/hr
        l = 1
        # upper speed bound: Max of piles
        r = max(piles)
        while l < r:
            m = l + (r - l) // 2
            # if speed is feasible => check if lower speed is feasible.
            if feasible(m):
                # r holds feasible upper bound 
                # we don't know if we will find a slower feasible speed
                r = m
            # else speed is to low => increase speed
            else:
                l = m + 1
        # does not matter if l or r since the while loop ends with l == r
        return l


TESTS = [
    # Format:
    (([3,6,7,11], 8,), 4),
    (([30,11,23,4,20], 5,), 30),
    (([30,11,23,4,20], 6,), 23),
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
