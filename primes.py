"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from ast import Raise
import math

def checkPrime(n):
    if n == 0 or n == 1:
        return False
    upperBound = int(math.sqrt(n)) + 1
    for i in range(2, upperBound):
        if n % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError

    list = []
    n = 2
    while len(list) != number_of_primes:
        if checkPrime(n):
            list.append(n)
        n += 1
    return list