#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determine the winner of each round
    Args:
        x: number of rounds
        nums: list of 'n' for each round
    Returns:
        The name of the player with the most wins or None if it's a draw
    """
    if x <= 0 or nums is None or not nums:
        return None

    ben = 0
    maria = 0

    max_num = max(nums)  # Find the largest number to optimize the sieve
    primes = sieve_of_eratosthenes(max_num)

    for n in nums:
        primes_count = sum(primes[:n + 1])

        # If the count of primes is even, Ben wins, otherwise Maria wins
        if primes_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes to find all primes up to n"""
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes

    for start in range(2, int(n ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False

    return sieve
