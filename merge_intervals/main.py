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
        intervals = sorted(intervals)
        stack = []
        for i in range(len(intervals)):
            curr = intervals[i]
            
            if stack:
                prev = stack.pop()
                start_prev, stop_prev = prev[0], prev[1]
                start_curr, stop_curr = curr[0], curr[1]
                
                # interval is overlapping if stop of prev is larger then start of current
                if stop_prev >= start_curr:
                    # need to pay attention to cases like: [1,4] and [2,3]
                    # need max end of interval
                    end = max(stop_curr, stop_prev)
                    stack.append([start_prev, end])
                else:
                    stack.append(prev)
                    stack.append(curr)
            else:
                stack.append(curr)
        
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
