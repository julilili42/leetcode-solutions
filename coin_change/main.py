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
METHOD = "coinChangeBottomUp"


class Solution:
    def coinChangeBottomUp(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == amount + 1:
            return -1

        return dp[amount]

    def coinChangeTopDown(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(total: int):
            if total == amount:
                return 0
            if total > amount:
                return amount + 1
            if total in mem:
                return mem[total]

            min_number = float("inf")
            for j in range(len(coins)):
                cur = 1 + dfs(total + coins[j])
                min_number = min(min_number, cur)

            mem[total] = min_number

            return mem[total]

        res = dfs(0)
        return -1 if res > amount else res


TESTS = [
    (
        (
            [1, 2, 5],
            11,
        ),
        3,
    ),
    (
        (
            [2],
            3,
        ),
        -1,
    ),
    (
        (
            [1],
            0,
        ),
        0,
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
