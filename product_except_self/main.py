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
METHOD = "productExceptSelf"


class Solution:
    # O(n) Runtime, O(1) Space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result
    
    # O(n) Runtime, O(n) Space
    def productExceptSelfSuffixPrefix(self, nums:List[int]) -> List[int]:
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

    # O(n) Runtime, O(n) Space
    def productExceptSelfZeroCount(self, nums: List[int]) -> List[int]:
        product = 1
        # since num_zeros = 1 and >= 2 are special cases we
        # need to keep track of the number of zeros.
        num_zeros = 0 
        for num in nums:
            if num == 0:
                num_zeros += 1
            else:
                product *= num
        # initialization of result array with zeros. This makes it easier for the 
        # case num_zeros = 1 and >= 2. 
        result = [0] * len(nums)
        for i in range(len(nums)): 
            # general case
            if num_zeros == 0:
                result[i] = int(product / nums[i])
            # special case num_zeros = 1
            elif num_zeros == 1 and nums[i] == 0:
                result[i] = product
            # special case num_zeros >= 2
        
        return result

    # O(n^2) Runtime
    def productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
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
