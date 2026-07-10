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
METHOD = "letterCombinations"


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(pos: int, s: str):
            if len(s) == len(digits):
                res.append(s)
                return
            if pos == len(digits):
                return

            letters = mapping.get(digits[pos], None)

            if not letters:
                return

            for letter in letters:
                dfs(pos + 1, s + letter)

        dfs(0, "")
        return res


TESTS = [
    (("23",), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    (("2",), ["a", "b", "c"]),
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
