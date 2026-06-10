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
METHOD = "isPalindrome"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch.lower()

        return new == new[::-1]

    def isPalindromeBruteForce(self, s: str) -> bool:
        from string import ascii_letters, digits
        s = "".join(ch.lower() for ch in s if ch in (ascii_letters + digits))
        return s == s[::-1]

    def isPalindromeSlow(self, s: str) -> bool:
        from string import ascii_letters, digits
        s = "".join(ch.lower() for ch in s if ch in (ascii_letters + digits))
        
        l = 0
        r = len(s) - 1
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1 
            else: 
                return False

        return True

    def isPalindromeRegex(self, s: str) -> bool:
        import re
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        
        l = 0
        r = len(s) - 1
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1 
            else: 
                return False

        return True

    def isPalindromeNoRegex(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()

        print(s)
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
        return True



TESTS = [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",), False),
    ((" ",), True),
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
