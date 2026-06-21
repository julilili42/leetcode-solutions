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
METHOD = "dailyTemperatures"


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            # stack contains index of previous temperatures
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                # calculate distance to next highest temperature 
                res[prev_index] = i - prev_index
            
            stack.append(i)
            
        return res
               





TESTS = [
    (([73,74,75,71,69,72,76,73],), [1,1,4,2,1,1,0,0]),
    (([30,40,50,60],), [1,1,1,0]),
    (([30,60,90],), [1,1,0]),
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
