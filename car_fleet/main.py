from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from math import inf, gcd
import sys
import math


# Change this to the LeetCode method name
METHOD = "carFleet"


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        metrics = sorted(zip(position, speed), reverse=True)
        
        for position, speed in metrics:
            remaining_distance = target - position
            # requires float division since cars can also catch up during non discrete timesteps
            remaining_time = remaining_distance / speed
            
            # car catches up if remaining_time <= time of fleet in front
            if not stack or remaining_time > stack[-1]:
                # if this is the case we have a fleet which is added to the stack
                stack.append(remaining_time)
            
        return len(stack) 


TESTS = [
    ((12, [10,8,0,5,3], [2,4,1,1,3],), 3),
    ((10, [3], [3],), 1),
    ((100, [0,2,4], [4,2,1],), 1),
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
