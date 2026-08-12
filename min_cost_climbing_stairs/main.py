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
METHOD = "minCostClimbingStairs"


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}

        def dfs(i: int):
            if i >= len(cost):
                return 0

            nonlocal mem
            if i in mem:
                return mem[i]

            one = cost[i] + dfs(i + 1)
            two = cost[i] + dfs(i + 2)

            mem[i] = min(one, two)

            return mem[i]

        return min(dfs(0), dfs(1))


TESTS = [
    (([10, 15, 20],), 15),
    (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
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
