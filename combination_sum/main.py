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
METHOD = "combinationSum"


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(s: int, i: int):
            # is s a solution? 
            if s == target:
                res.append(subset.copy())
                return
            # is the path invalid? 
            elif s > target:
                return
            # no more solutions? 
            elif i >= len(candidates):
                return


            # take candidate
            subset.append(candidates[i])
            dfs(s + candidates[i], i)

            # skip candidate
            subset.pop()
            dfs(s, i + 1)

        dfs(0, 0)
        return res


TESTS = [
    (([2,3,6,7], 7,), [[2,2,3],[7]]),
    (([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]]),
    (([2], 1), []),
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
