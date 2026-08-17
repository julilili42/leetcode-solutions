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
METHOD = "partitionLabelsClean"


class Solution:
    def partitionLabelsClean(self, s: str) -> List[int]:
        positions = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        res = []

        for i, ch in enumerate(s):
            end = max(end, positions[ch])

            if i == end:
                res.append((end + 1) - start)
                start = i + 1

        return res

    def partitionLabels(self, s: str) -> List[int]:
        positions = {}

        for i, ch in enumerate(s):
            positions[ch] = i

        idx = -1
        res = []
        for i, ch in enumerate(s):
            last = positions[ch]
            idx = max(idx, last)

            if i == idx:
                prev = sum(res)
                res.append((idx + 1) - prev)
                idx = -1

        return res


TESTS = [
    (("ababcbacadefegdehijhklij",), [9, 7, 8]),
    (("eccbbbbdec",), [10]),
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
