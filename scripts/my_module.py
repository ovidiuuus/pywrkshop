""" This Script computes the sum of factorial of a list of numbers """
import math

def compute(numbers):
    return([math.factorial(n) for n in numbers])