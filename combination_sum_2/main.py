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
METHOD = "combinationSum2"


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []

        candidates = sorted(candidates)

        def dfs(index: int, total: int):
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return
            if index == len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                subset.pop()

        dfs(0, 0)

        return res


TESTS = [
    (
        (
            (
                [10, 1, 2, 7, 6, 1, 5],
                8,
            ),
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        )
    ),
    (
        (
            [2, 5, 2, 1, 2],
            5,
        ),
        [[1, 2, 2], [5]],
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
