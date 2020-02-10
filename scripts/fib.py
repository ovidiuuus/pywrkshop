"""
This module calculates the fibonacci sequence
"""

def fib_iter(n):
    prev = 0
    curr = 1
    for i in range(n-1):
        curr_old = curr
        curr = prev + curr
        prev = curr_old
    return curr

