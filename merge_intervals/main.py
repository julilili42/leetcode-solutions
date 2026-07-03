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
METHOD = "merge"


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # two intervals [a,b] and [c,d] overlapp if b >= c
        # if this is the case we merge to [a, max(b, d)]
        # neeed to make sure a < c to compare them => sorting
        # need to compare to predecessor intervall => stack

        intervals = sorted(intervals)

        stack = []

        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            
            a, b = stack[-1]
            c, d = interval

            if b >= c:
                stack.pop()
                stack.append([a, max(b, d)])
            else:
                stack.append([c, d])

        return stack

TESTS = [
    (([[1,3],[2,6],[8,10],[15,18]], ), [[1,6],[8,10],[15,18]]),
    (([[1,4],[4,5]], ), [[1,5]]),
    (([[4,7],[1,4]],), [[1,7]]),
    (([[1,4],[2,3]],), [[1,4]]),
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
