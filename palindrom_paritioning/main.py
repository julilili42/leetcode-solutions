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
METHOD = "partition"


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrom(s: str):
            return s == s[::-1]

        res = []
        subset = []

        def dfs(i: int):
            if i == len(s):
                res.append(subset.copy())
                return

            for j in range(i + 1, len(s) + 1):
                candidate = s[i:j]
                if is_palindrom(candidate):
                    subset.append(candidate)
                    dfs(j)
                    subset.pop()

        dfs(0)
        return res


TESTS = [
    (("aab",), [["a", "a", "b"], ["aa", "b"]]),
    (("a",), [["a"]]),
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
