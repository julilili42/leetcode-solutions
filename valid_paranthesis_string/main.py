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
METHOD = "checkValidString"


class Solution:
    def checkValidString(self, s: str) -> bool:
        mem = {}

        def dfs(i: int, total: int):
            if i == len(s):
                return total == 0
            if total < 0:
                return False

            key = (i, total)
            if key in mem:
                return mem[key]

            ch = s[i]
            if ch == "(":
                mem[key] = dfs(i + 1, total + 1)
            elif ch == ")":
                mem[key] = dfs(i + 1, total - 1)
            else:
                mem[key] = (
                    dfs(i + 1, total + 1) or dfs(i + 1, total - 1) or dfs(i + 1, total)
                )

            return mem[key]

        return dfs(0, 0)


TESTS = [
    (("()"), True),
    (("(*)"), True),
    (("(*))"), True),
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
