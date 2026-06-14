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
METHOD = "groupAnagrams"


class Solution:
    # instead of using a string fingerprint we could also use a tuple as fingerprint. This makes the fingerprint calculation
    # much easier. 
    # Since tuples are immutable, they are hashable and we can use them as keys for our buckets
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            map[tuple(count)].append(s)

        return list(map.values())


    def groupAnagramsSorting(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            # sorted anagrams are equal to each other
            # sort string and use it as key for the groups
            s_sorted = "".join(sorted(s))
            groups[s_sorted].append(s)

        return list(groups.values())

    
    def computeFingerprintString(self, s: str) -> List[List[str]]:
        count = [0] * 26
        
        # calculate frequency of each character in string
        for c in s:
            count[ord(c) - ord("a")] += 1

        # list of [char1, freq1, char2, freq2, ...]
        res = []
        for i in range(26):
            if count[i] != 0:
                res.extend([chr(i + ord("a")), str(count[i])])
        # since list are not hashable we convert list into string: "char1freq1char2freq2..."
        # we will use this string as the fingerprint of an bucket later 
        return "".join(res)


    def groupAnagramsFingerprint(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            groups[self.computeFingerprintString(s)].append(s)

        return list(map.values())
    

    

TESTS = [
    ((["eat","tea","tan","ate","nat","bat"],), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    (([""],), [[""]]),
    ((["a"],), [["a"]])
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
