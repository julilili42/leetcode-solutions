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
METHOD = "reorganizeString"


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1

        heap = []
        for c, f in freq.items():
            heappush(heap, (-f, c))

        res = ""
        prev = None
        while heap:
            print(heap[0])
            (f, ch) = heappop(heap)
            if prev:
                heappush(heap, prev)

            res += ch
            f += 1
            prev = (f, ch) if f < 0 else None

        return "" if len(s) != len(res) else res


TESTS = [
    (("aab",), "aba"),
    (("aaab",), ""),
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
