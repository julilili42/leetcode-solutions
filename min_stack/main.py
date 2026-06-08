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
METHOD = "solve"


class Solution:
    def __init__(self):
        # first index => value
        # second index => current min_value
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((value, value))
        else:
            top, min_value = self.stack[-1]
            min_value = min(min_value, value)

            self.stack.append((value, min_value))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        top, _ = self.stack[-1]
        return top

    def getMin(self) -> int:
        _, min_value = self.stack[-1]
        return min_value

TESTS = []


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
