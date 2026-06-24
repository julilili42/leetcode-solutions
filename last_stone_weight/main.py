from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest
from math import inf, gcd
import sys


# Change this to the LeetCode method name
METHOD = "lastStoneWeight"


class Solution:
    # use max heap by pushing negative weights on min heap
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)
        
        while len(heap) > 1:
            s1 = -heappop(heap)
            s2 = -heappop(heap)
            # if s1 == s2 both stones should be destroyed. This is already the 
            # case since we pop both stones from the heap
            if s1 != s2:
                # since s1 != s2 and s1 is poped first we know that s1 > s2.
                # push -(s2 - s1) since we have a max heap
                heappush(heap, -(s2 - s1))

        return -heap[0] if heap else 0



TESTS = [
    (([2,7,4,1,8,1], ), 1),
    (([1], ), 1),
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
