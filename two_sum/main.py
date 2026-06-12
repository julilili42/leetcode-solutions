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
METHOD = "twoSum"


class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summation = {}

        for i in range(len(nums)):
            number = nums[i]
            summation[target - number] = i
        

        for i in range(len(nums)):
            found_index = summation.get(nums[i], -1)
            # we have to make sure to not pick the same index twice. 
            # This can happen since we iterate through the array and might 
            # reference to the same number which we currently on.
            # F.ex.: [3,2,4] target: 6
            # summation = {3: 0, 4: 1, 2: 2}
            # Starting the loop at nums[0] = 3 gives us 0 => [0,0] is returned 
            # which is not allowed
            if found_index != -1 and found_index != i:
                return [i, found_index]

        return [-1,-1]



TESTS = [
    (([2,7,11,15], 9), [0,1]),
    (([3,2,4], 6), [1,2]),
    (([3,3], 6), [0,1]),
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
