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
METHOD = "characterReplacement"


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        max_length = 1
        # max_freq is not always the exact max_frequency in the current window.
        # it is the highest freq we have seen while expanding the window. 
        # that is sufficient since we only care about the max_length, 
        # not if the current window is valid. 
        # alternatively: use max_freq = max(freq.values())
        max_freq = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            # to minimize the changes in the window, we need to identify the
            # character with the highest frequency. 
            max_freq = max(freq[s[r]], max_freq)

            # the minimum number of changes is then given by 
            # current_length - max_frequency 
            while (r - l + 1) - max_freq > k:
                # if we have more then k needed changes, the window is invalid. 
                # therefore we need to shrink the window from the left
                freq[s[l]] -= 1
                l += 1
        
            max_length = max(max_length, r - l + 1)

        return max_length

TESTS = [
    (("ABAB",2,), 4),
    (("AABABBA",1,), 4),
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
