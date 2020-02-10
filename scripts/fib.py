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

def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
