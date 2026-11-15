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
METHOD = "longestCommonSubsequence"


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        n, m = len(text1), len(text2)

        def dfs(i: int, j: int):
            if i == n or j == m:
                return 0
            key = (i, j)
            if key in mem:
                return mem[key]

            if text1[i] == text2[j]:
                mem[key] = 1 + dfs(i + 1, j + 1)
            else:
                mem[key] = max(dfs(i + 1, j), dfs(i, j + 1))

            return mem[key]

        return dfs(0, 0)


TESTS = [
    (("abcde", "ace"), 3),
    (("abc", "abc"), 3),
    (("abc", "def"), 3),
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
