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
METHOD = "eraseOverlapIntervalsClean"


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        stack = []
        res = 0

        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue

            a, b = stack[-1]
            c, d = interval

            if c < b:
                res += 1

                if d < b:
                    stack[-1] = interval
            else:
                stack.append(interval)

        return res

    def eraseOverlapIntervalsClean(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                res += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return res


TESTS = [
    (([[1, 2], [2, 3], [3, 4], [1, 3]],), 1),
    (([[1, 2], [1, 2], [1, 2]],), 2),
    (([[1, 2], [2, 3]],), 0),
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
