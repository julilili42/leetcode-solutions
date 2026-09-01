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
METHOD = "wordBreak"


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        mem = {}

        def dfs(i: int):
            if i == len(s):
                return True

            if i in mem:
                return mem[i]

            for j in range(i, len(s)):
                # takes O(n) in python
                cur = s[i : j + 1]
                if cur not in words:
                    continue
                if dfs(j + 1):
                    return True

            mem[i] = False
            return mem[i]

        return dfs(0)


TESTS = [
    (("leetcode", ["leet", "code"]), True),
    (("applepenapple", ["apple", "pen"]), True),
    (("leetcode", ["leet", "code"]), True),
    (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
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
