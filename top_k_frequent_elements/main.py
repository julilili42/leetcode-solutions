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
        n = len(nums)

        buckets = [[] for _ in range(n + 1)]

        for value, freq in counter.items():
            buckets[freq].append(value)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for value in bucket:
                if len(result) < k: 
                    result.append(value)
        
        return result
            

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
