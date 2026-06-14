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
METHOD = "lengthOfLongestSubstring"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_length = 0

        # we will expand the window to the right...
        for r in range(len(s)):
            
            # ... until we encounter a character s[r] which was already seen.
            while s[r] in seen:
            # We narrow down the window from the left until s[r] is not in  
            # seen anymore. 
                seen.discard(s[l])
                l += 1

            # If s[r] is not in seen we can add s[r]
            seen.add(s[r])
            max_length = max(max_length, r - l + 1)
        
        return max_length


    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        max_length = 0

        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                else:
                    chars.add(s[j])
                    max_length = max(max_length, len(chars))

        return max_length




TESTS = [
    (("abcabcbb",), 3),
    ((" ",), 1),
    (("ab",), 2),
    (("dvdf",), 3),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
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
