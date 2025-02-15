"""
Solving Leetcode Problem.
https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

Given two positive integers startPos and endPos
Initially, you are standing at position startPos on an infinite
number line. With one step, you can move either one position to the left,
or one position to the right.

Given a positive integer k, return the number of different ways to
reach the position endPos starting from startPos, such that you
perform exactly k steps.
"""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
def solve(startPos, endPos, k):
    if k < endPos - startPos or (k - (endPos - startPos)) % 2 != 0:
        return 0
    
    # a: number of steps to the right, b: number of steps to the left
    a = (k + endPos - startPos) // 2
    b = k - a 
    return factorial(a + 1) // (factorial(b) * factorial(a + 1 - b))

if __name__ == "__main__":
    print(solve(1, 3, 6))

    

