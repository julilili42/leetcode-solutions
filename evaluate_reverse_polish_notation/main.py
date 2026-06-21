from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from math import inf, gcd
import sys
import operator



# Change this to the LeetCode method name
METHOD = "evalRPN"


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"*", "/", "+", "-"}:
                right = stack.pop()
                left = stack.pop()
                
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(token))

        return stack[-1]

    def evalRPNImport(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        for token in tokens:
            if not stack:
                stack.append(token)
                continue
            
            # if we encounter a operator we pop both elements
            # and execute the operator on it.
            if token in operators.keys():
                op = operators[token]
                right = stack.pop()
                left = stack.pop()
                result = op(int(left), int(right))
                    
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack[-1])

TESTS = [
    ((["2","1","+","3","*"],), 9),
    ((["4","13","5","/","+"],), 6),
    ((["10","6","9","3","+","-11","*","/","*","17","+","5","+"],), 22),
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
