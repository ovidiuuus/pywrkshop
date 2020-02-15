"""
This module calculates the fibonacci sequence in multiple ways
"""
import time as tn

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

### Activity 12: Fibonacci Function iwth Dynamic Programming
fib_sec = {}
def fib_dyn(n):
    if n == 1 or n == 2:
        fib_sec[1] = 1
        fib_sec[2] = 1
        return 1
    else:
        if (n-1) not in fib_sec:
            fib_dyn(n - 1)
        if (n - 2) not in fib_sec:
            fib_dyn(n - 2)
        fib_sec[n] = fib_sec[n - 1] + fib_sec[n - 2]
    return fib_sec[n]

def fib_rec_sec(n):
    start_tn = tn.perf_counter()
    print("FIB[", n, "] = ", fib_rec(n) ,"and was executed in", tn.perf_counter() - start_tn, "seconds!")

def fib_dyn_sec(n):
    start_tn = tn.perf_counter()
    print("FIB[", n, "] = ", fib_dyn(n) ,"and was executed in", tn.perf_counter() - start_tn, "seconds!")

