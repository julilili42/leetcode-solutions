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
METHOD = "isNStraightHand"


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)
        for start in sorted(count):
            # number of sequences which start at card start.
            freq = count[start]

            if freq == 0:
                continue
            # since we start at `start` there have to be cards
            # `start`...`start + groupSize` s.t. we can have a group of
            # size groupSize. If any of those cards have a freq which is
            # smaller then the start freq, then we are not able to cover the
            # set of cards by groups of size groupSize.
            for num in range(start, start + groupSize):
                if count[num] < freq:
                    return False

                count[num] -= freq

        return True

    def isNStraightHandFirst(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        heap = []
        counter = Counter(hand)

        for val, freq in counter.items():
            heappush(heap, (val, freq))

        temp = []
        q = deque()
        while heap:
            val, freq = heappop(heap)
            q.append((val, freq - 1))
            temp.append(val)
            n = len(temp)

            if n > 1:
                if val != temp[-2] + 1:
                    return False

            if n == groupSize:
                while q:
                    val, freq = q.popleft()
                    if freq != 0:
                        heappush(heap, (val, freq))

                temp = []

        return len(temp) == 0


TESTS = [
    (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
    (([1, 2, 3, 4, 5], 4), False),
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
