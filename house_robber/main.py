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
METHOD = "rob"


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i: int, prev_taken: bool):
            if i == len(nums):
                return 0
            key = (i, prev_taken)
            if key in memo:
                return memo[key]

            skip = dfs(i + 1, False)
            take = 0 if prev_taken else nums[i] + dfs(i + 1, True)

            memo[key] = max(skip, take)

            return memo[key]

        return dfs(0, False)


TESTS = [
    (([1, 2, 3, 1],), 4),
    (([2, 7, 9, 3, 1],), 12),
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
