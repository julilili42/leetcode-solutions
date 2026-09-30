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
METHOD = "leastInterval"


class Solution:
    # task order execution is arbitrary
    # >= n intervals between two tasks with same label
    # find min. number of intervals to complete all tasks
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []
        cooldown = deque()
        i = 0

        for label, freq in counter.items():
            heappush(heap, -freq)

        while heap or cooldown:
            if heap:
                freq = -heappop(heap)
                if freq > 1:
                    cooldown.append((freq - 1, n + i + 1))

            i += 1

            while cooldown and cooldown[0][1] == i:
                freq, _ = cooldown.popleft()
                heappush(heap, -freq)

        return i


TESTS = [
    ((["A", "A", "A", "B", "B", "B"], 2), 8),
    ((["A", "C", "A", "B", "D", "B"], 1), 6),
    ((["A", "A", "A", "B", "B", "B"], 3), 10),
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
