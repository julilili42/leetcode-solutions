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
METHOD = "isValid"


class Solution:
    brackets = {"(":")", "{": "}", "[": "]"}

    def isValid(self, s: str) -> bool:
        stack = []
        p = 0
        while p < len(s):
            peak = None
            if len(stack) > 0:
                peak = stack[-1]
            
            matching_peak = self.brackets.get(peak, None)
            bracket = s[p]
            
            if matching_peak == bracket:
                popped = stack.pop()
            else:
                stack.append(bracket)
        
            p += 1

        return len(stack) == 0

TESTS = [
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([])",), True),
    (("([)]",), False),
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
