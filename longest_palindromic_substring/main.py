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
METHOD = "longestPalindrome"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        def expand(l: int, r: int):
            nonlocal longest

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l : r + 1]

                l -= 1
                r += 1

            return longest

        for i in range(n):
            # uneven
            expand(i, i)
            # even
            expand(i, i + 1)

        return longest


TESTS = [
    (("babad"), "bab"),
    (("cbbd"), "bb"),
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
