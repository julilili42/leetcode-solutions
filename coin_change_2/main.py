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
METHOD = "changeTopDown"


class Solution:
    def changeTopDown(self, amount: int, coins: List[int]) -> int:
        mem = {}

        def dfs(i: int, total: int):
            if total == amount:
                return 1
            if total > amount or i == len(coins):
                return 0

            key = (i, total)
            if key in mem:
                return mem[key]

            mem[key] = dfs(i + 1, total) + dfs(i, total + coins[i])

            return mem[key]

        return dfs(0, 0)


TESTS = [
    (
        (
            5,
            [1, 2, 5],
        ),
        4,
    ),
    (
        (
            3,
            [2],
        ),
        0,
    ),
    (
        (
            10,
            [10],
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
