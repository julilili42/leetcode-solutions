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


class RandomizedSet:
    def __init__(self):
        self.hash_set = {}
        self.list_set = []

    def insert(self, val: int) -> bool:
        idx = self.hash_set.get(val, None)
        if idx is None:
            self.hash_set[val] = len(self.list_set)
            self.list_set.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        idx = self.hash_set.get(val, None)
        if idx is None:
            return False

        # last element in list
        last_element = self.list_set[-1]

        # overwrite list entry at idx with last element
        self.list_set[idx] = last_element
        self.hash_set[last_element] = idx

        # delete entries
        self.hash_set.pop(val)
        self.list_set.pop()

        return True

    def getRandom(self) -> int:
        from random import randrange

        random_idx = randrange(len(self.list_set))
        return self.list_set[random_idx]


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
