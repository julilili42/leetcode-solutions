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
METHOD = "jump"


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}

        def dfs(i: int):
            if i >= n - 1:
                return 0

            if i in mem:
                return mem[i]

            min_jumps = float("inf")
            for j in range(1, nums[i] + 1):
                cur = 1 + dfs(i + j)
                min_jumps = min(min_jumps, cur)

            mem[i] = min_jumps
            return mem[i]

        return dfs(0)


TESTS = [
    (([2, 3, 1, 1, 4],), 2),
    (([2, 3, 0, 1, 4],), 2),
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
