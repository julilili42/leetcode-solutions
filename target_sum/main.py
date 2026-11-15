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
METHOD = "findTargetSumWays"


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        mem = {}
        n = len(nums)

        def dfs(i: int, total: int):
            if i == n:
                if total == target:
                    return 1
                else:
                    return 0

            key = (i, total)
            if key in mem:
                return mem[key]

            plus = dfs(i + 1, total + nums[i])
            minus = dfs(i + 1, total - nums[i])

            mem[key] = plus + minus

            return mem[key]

        return dfs(0, 0)


TESTS = [
    (
        (
            [1, 1, 1, 1, 1],
            3,
        ),
        5,
    ),
    (
        (
            [1],
            1,
        ),
        1,
    ),
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
