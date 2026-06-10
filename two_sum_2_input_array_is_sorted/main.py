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
METHOD = "twoSumDictionary"


class Solution:
    def twoSumTwoPointer(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1
        
        return [-1, -1]
    
    
    def twoSumDictionary(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        
        for i in range(len(numbers)):
            current = numbers[i]
            if target - current in d:
                return [d[target - current] + 1, i + 1]
            d[current] = i




TESTS = [
    (([2,7,11,15], 9,), [1,2]),
    (([2,3,4], 6,), [1,3]),
    (([-1,0], -1,), [1,2]),
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
