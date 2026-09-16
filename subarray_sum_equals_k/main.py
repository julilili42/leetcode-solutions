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
METHOD = "subarraySum"


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix_sums = {}
        total = 0
        res = 0
        for n in nums:
            total += n
            if total == k:
                res += 1
            if total - k in prefix_sums:
                res += prefix_sums[total - k]

            prefix_sums[total] = 1 + prefix_sums.get(total, 0)

        return res

    # O(n^2) solution does not pass
    def subarraySumSlow(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        cfd = [0] * n
        s = 0
        for i in range(n):
            s += nums[i]
            cfd[i] = s

        for i in range(n):
            total = 0
            for j in range(i, n):
                total = cfd[j] - (cfd[i - 1] if i > 0 else 0)
                if total == k:
                    res += 1

        return res


TESTS = [
    (
        (
            [1, 1, 1],
            2,
        ),
        2,
    ),
    (
        (
            [1, 2, 3],
            3,
        ),
        2,
    ),
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
