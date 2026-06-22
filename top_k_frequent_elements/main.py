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
METHOD = "topKFrequent"


class Solution:
    def topKFrequentBruteForce(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = list({k:v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)})
        return sorted_freq[0:k]
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        # we need len(nums) + 1 buckets, since f.ex. [1,1,1,2,2,3] could have
        # frequencies ranging from 0, ..., 5, 6. This gives us a frequency 
        # array with 7 buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for value, freq in counter.items():
            buckets[freq].append(value)
        
        # since we have 7 buckets (0, ..., 5, 6) we need to start with
        # len(buckets) - 1 and iterate until 0. 
        # Reverse iteration range(len(buckets) - 1, -1, -1): 
        # [len(buckets) - 1, -1) => [6...0]
        # Normal iteration range(len(buckets)): 
        # [0, len(buckets) + 1) => [0 ...6] 
        res = []
        for i in range(len(buckets) - 1, -1, -1): 
            # this could return a res with len(res) > k since we add bucket
            # without knowing how many elements are in bucket
            """bucket = buckets[i]
            if len(res) < k:
                res.extend(bucket)
            """
            # to make sure len(res) is equal to k
            for val in buckets[i]:
                res.append(val)

                if len(res) == k:
                    return res
            

TESTS = [
    (([1,1,1,2,2,3], 2), [1,2]),
    (([1], 1), [1]),
    (([1,2,1,2,1,2,3,1,3,2], 2), [1,2]),
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
