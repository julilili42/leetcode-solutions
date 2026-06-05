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


    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # start counting at the beginning of a sequence
            if (num - 1) not in num_set:
                length = 1
                start = num + 1

                while start in num_set:
                    length += 1
                    start += 1
                
                max_length = max(max_length, length)

        return max_length


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
