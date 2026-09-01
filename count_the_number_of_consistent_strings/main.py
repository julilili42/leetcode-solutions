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
METHOD = "countConsistentStrings"


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0

        for w in words:
            consistent = True
            for ch in w:
                if ch not in allowed:
                    consistent = False
                    break

            if consistent:
                res += 1

        return res


TESTS = [
    (
        (
            "ab",
            ["ad", "bd", "aaab", "baa", "badab"],
        ),
        2,
    ),
    (
        (
            "abc",
            ["a", "b", "c", "ab", "ac", "bc", "abc"],
        ),
        7,
    ),
    (
        (
            "cad",
            ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],
        ),
        4,
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
