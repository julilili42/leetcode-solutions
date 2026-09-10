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
METHOD = "lengthOfLIS"


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}
        n = len(nums)

        def dfs(i: int):
            if i in mem:
                return mem[i]

            best = 1

            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            mem[i] = best
            return mem[i]

        return max(dfs(i) for i in range(n))


TESTS = [
    (([10, 9, 2, 5, 3, 7, 101, 18]), 4),
    (([0, 1, 0, 3, 2, 3]), 4),
    (([7, 7, 7, 7, 7, 7, 7]), 1),
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
