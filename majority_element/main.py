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
METHOD = "majorityElement"


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        score = 0
        element = nums[0]
        for num in nums:
            if num == element:
                score += 1
            else:
                score -= 1

            if score < 0:
                element = num
                score = 0

        return element


TESTS = [
    (([3, 2, 3]), 3),
    (([2, 2, 1, 1, 1, 2, 2]), 2),
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
