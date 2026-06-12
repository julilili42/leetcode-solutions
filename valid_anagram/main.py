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
METHOD = "isAnagram"


class Solution:
    def isAnagramTrivial(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        # is needed since zip(s,t) number of iterations = min(len(s), len(t))
        # this would accept f.ex. s = "a" and t = "ab"
        if len(s) != len(t):
            return False
        
        occurences = defaultdict(int)
        
        for s_letter, t_letter in zip(s,t):
            occurences[s_letter] += 1
            occurences[t_letter] -= 1

        for letter, freq in occurences.items():
            if freq != 0:
                return False
        
        return True
    
    # same logic using array instead of dictionary
    def isAnagramAlphabet(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabet = [0] * 26

        for s_char, t_char in zip(s,t):
            alphabet[ord(s_char) - ord("a")] += 1
            alphabet[ord(t_char) - ord("a")] -= 1


        for freq in alphabet:
            if freq != 0:
                return False
        
        return True



TESTS = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
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
