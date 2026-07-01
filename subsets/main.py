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
METHOD = "subsets"


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []     
        subset = []
       
       
        def dfs(i):
            if i == len(nums):
                # append subset if leaf nodes are reached
                # need to copy since value changes and we want to freeze subset of recursive call instead
                # of referencing it
                res.append(subset.copy())
                return

            # include nums[i] into subset
            subset.append(nums[i])
            # continue decision tree including nums[i]
            dfs(i + 1)
            
            # reverse taking nums[i]
            subset.pop()
            # continue decision tree without nums[i]
            dfs(i + 1)
        
        dfs(0)

        return res

TESTS = [
    (([1,2,3],), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    (([0],), [[],[0]]),
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
