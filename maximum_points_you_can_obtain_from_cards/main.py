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
METHOD = "maxScore"


class Solution:
    # maximize score = minimize sum of sliding window with size n - k
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        total = sum(cardPoints)
        end = n - window_size + 1

        # initialize with sum of first iteration l = 0
        starting_sum = sum(cardPoints[:window_size])
        window_sum = starting_sum
        res = starting_sum

        for l in range(1, end):
            window_sum -= cardPoints[l - 1]
            window_sum += cardPoints[l + window_size - 1]

            res = min(res, window_sum)

        return total - res

    def maxScoreRecursion(self, cardPoints: List[int], k: int) -> int:
        mem = {}

        def dfs(l: int, r: int, steps: int):
            if steps == k:
                return 0

            key = (l, r, steps)
            if key in mem:
                return mem[key]

            left = cardPoints[l] + dfs(l + 1, r, steps + 1)
            right = cardPoints[r] + dfs(l, r - 1, steps + 1)

            mem[key] = max(left, right)
            return mem[key]

        return dfs(0, len(cardPoints) - 1, 0)


TESTS = [
    (
        (
            [1, 2, 3, 4, 5, 6, 1],
            3,
        ),
        12,
    ),
    (
        (
            [2, 2, 2],
            2,
        ),
        4,
    ),
    (
        (
            [9, 7, 7, 9, 7, 7, 9],
            7,
        ),
        55,
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
