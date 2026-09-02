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
METHOD = "kthDistinct"


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        count = 0
        for ch in arr:
            if freq[ch] == 1:
                if count == k - 1:
                    return ch
                else:
                    count += 1

        return ""


TESTS = [
    ((["d", "b", "c", "b", "c", "a"], 2), "a"),
    ((["aaa", "aa", "a"], 1), "aaa"),
    ((["a", "b", "a"], 3), ""),
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
