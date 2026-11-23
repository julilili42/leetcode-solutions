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


class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]

        cur["*"] = ""

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return "*" in node

            ch = word[i]

            if ch == ".":
                for key, child in node.items():
                    if key != "*" and dfs(i + 1, child):
                        return True
                return False

            if ch not in node:
                return False

            return dfs(i + 1, node[ch])

        return dfs(0, self.trie)


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
