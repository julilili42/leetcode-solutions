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
METHOD = "solve"


class TimeMap:
    def __init__(self):
        self.store = {}

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        m = self.store.get(key, None)
        if not m:
            self.store[key] = [(value, timestamp)]
        else:
            m.append((value, timestamp))

    # O(log(n))
    def get(self, key: str, timestamp: int) -> str:
        data = self.store.get(key, None)
        if not data:
            return ""

        l = 0
        r = len(data) - 1
        best = -1

        while l <= r:
            m = l + (r - l) // 2

            if data[m][1] == timestamp:
                return data[m][0]
            elif data[m][1] < timestamp:
                best = m
                l = m + 1
            else:
                r = m - 1

        return "" if best == -1 else data[best][0]


# we could also use only r since
# r points at largest timestamp <= timestamp
# while
# l points at first timestamp > timestamp


class TimeMap:
    def __init__(self):
        self.store = {}

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        m = self.store.get(key, None)
        if not m:
            self.store[key] = [(value, timestamp)]
        else:
            m.append((value, timestamp))

    # O(log(n))
    def get(self, key: str, timestamp: int) -> str:
        data = self.store.get(key, None)
        if not data:
            return ""

        l = 0
        r = len(data) - 1

        while l <= r:
            m = l + (r - l) // 2

            if data[m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1

        return "" if r < 0 else data[r][0]


TESTS = [
    # Format:
    # ((arg1, arg2, ...), expected),
    # Example:
    # (([2, 7, 11, 15], 9), [0, 1]),
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
