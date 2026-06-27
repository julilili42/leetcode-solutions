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
METHOD = "checkInclusion"


class Solution:

    # Runtime O(n*m) where n = len(s1) and m = len(s2)
    def checkInclusionBruteForce(self, s1: str, s2: str) -> bool:
        def calculate_fingerprint(s) -> list[int]:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord("a")] += 1

            return freq

        freq_s1 = calculate_fingerprint(s1)

        l = 0

        for r in range(len(s2)):
            # substring in string s2
            current = s2[l:r + 1] if r + 1 < len(s2) else s2[l:len(s2)]
            
            freq_s2 = self.calculate_fingerprint(current)
            
            if freq_s2 == freq_s1:
                return True

            if (r - l + 1) >= len(s1):
                l += 1
        
        return False


    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def calculate_fingerprint(s) -> list[int]:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord("a")] += 1

            return freq
    
        s1_fp = calculate_fingerprint(s1)
        window_fp = [0] * 26
        l = 0
    
        for r in range(len(s2)):    
            # check if current window is larger then s1
            if (r - l + 1) > len(s1):
                # decrease counter of first character in window
                window_fp[ord(s2[l]) - ord("a")] -= 1   
                # and decrease window size 
                l += 1
            
            # increase counter of new character 
            window_fp[ord(s2[r]) - ord("a")] += 1
            

            # if both fingerprints match it implies that s2 has a substring with the same amount of characters 
            # therefore s1 is a permutation of the current substring of s2
            if window_fp == s1_fp:
                return True
        
        return False
        

        

            



TESTS = [
    (("ab", "eidbaooo",), True),
    (("adc", "dcda",), True),
    (("ab", "eidboaoo",), False),
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
