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
METHOD = "longestConsecutive"


class Solution:
    # O(n) since the sequence starts with the smallest element. Each element is iterated through only once
    # as a successor.
    def longestConsecutive(self, nums: List[int]) -> int:
        # sets have O(1) read/write.
        # duplicates can be ignored since they do not add the length of 
        # consecutive elements.
        nums = set(nums)
        max_length = 0
        # if nums is empty we skip the for-loop and return 0.
        for num in nums:
            # longest consecutive sequence starts with element which does not 
            # have a predecessor. We need to check those sequences where the
            # predecessor is missing. 
            if (num - 1) not in nums:
                start = num + 1
                # since we entered the for loop the length is atleast one. 
                length = 1
                # check and keep track of consecutive elements. 
                while start in nums:
                    start += 1 
                    length += 1
                # update max_length only if we found the start of a new sequence.
                # Unecessary to update for each character since >1 possible only if no predecessor. 
                max_length = max(max_length, length)

        return max_length

    
    def longestConsecutiveBruteForce(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums) 
        
        if len(sorted_nums) == 0:
            return 0

        seq = 1
        longest_seq = 1

        for p in range(1, len(sorted_nums)):
            current = sorted_nums[p]
            prev = sorted_nums[p-1]
    
            if current == prev + 1:
                seq += 1
                longest_seq = max(seq, longest_seq)
            elif current == prev:
                continue
            else:
                seq = 1

        return longest_seq


    

TESTS = [
    (([100,4,200,1,3,2],), 4),
    (([0,3,7,2,5,8,4,6,0,1],), 9),
    (([1,0,1,2],), 3),
    (([1,2,6,7,8],), 3),
    (([0],), 1)
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
