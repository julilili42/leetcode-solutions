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
METHOD = "canPartition"


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False

        subset_sum = sum_ // 2
        n = len(nums)
        mem = {}

        def dfs(i: int, total: int):
            if total == subset_sum:
                return True
            if total > subset_sum:
                return False
            if i == n:
                return total == subset_sum
            key = (i, total)
            if key in mem:
                return mem[key]

            mem[key] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

            return mem[key]

        return dfs(0, 0)


TESTS = [
    (([1, 5, 11, 5],), True),
    (([1, 2, 3, 5],), False),
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
