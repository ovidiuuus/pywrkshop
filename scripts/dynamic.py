#Exercise 52 : Summing integers
###
# Timing the execution of the python code
###

import time

stored_results = {}
def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        if (i + 1) in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    print(time.perf_counter() - start_time, "seconds")
    return resulte