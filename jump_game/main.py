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
METHOD = "canJumpGreedy"


class Solution:
    def canJumpGreedy(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True

    def canJump(self, nums: List[int]) -> bool:
        mem = {}

        def dfs(i: int):
            if i == len(nums) - 1:
                return True

            if i in mem:
                return mem[i]

            for j in range(1, nums[i] + 1):
                if (i + j) < len(nums):
                    if dfs(i + j):
                        mem[i] = True
                        return True

            mem[i] = False
            return False

        return dfs(0)


TESTS = [
    (([2, 3, 1, 1, 4]), True),
    (([3, 2, 1, 0, 4]), False),
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
