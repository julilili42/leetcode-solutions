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
METHOD = "productExceptSelfNoDivision"


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            result[i] = product 
        return result
    
    def productExceptSelfFast(self, nums: List[int]) -> List[int]:
        product = 1
        zero_counter = 0
       
        for i in range(len(nums)):
            if num[i] == 0:
                zero_counter += 1
            else:
                product *= num[i]

        result = [0] * len(nums)
        for i in range(len(nums)):
            if zero_counter == 0:
                result[i] = int(product / nums[i])
            elif zero_counter == 1 and nums[i] == 0:
                result[i] = product
        
        return result

    def productExceptSelfNoDivision(self, nums:List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

TESTS = [
    (([1,2,4,6],), [48,24,12,8]),
    (([-1,0,1,2,3],), [0,-6,0,0,0]) 
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
