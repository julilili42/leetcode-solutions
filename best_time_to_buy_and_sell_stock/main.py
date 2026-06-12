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
METHOD = "maxProfit"


class Solution:
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            j = i + 1
            while j < len(prices):
                sell = prices[j]
                profit = sell - buy
                max_profit = max(max_profit, profit)
                j += 1
        
        return max_profit

    
    def maxProfitCorrect(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
           min_price = min(price, min_price) 
           profit = price - min_price
           max_profit = max(max_profit, profit)
        
        return max_profit
    
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices[1::]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit

TESTS = [
    (([7,1,5,3,6,4],), 5),
    (([7,6,4,3,1],), 0),
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
