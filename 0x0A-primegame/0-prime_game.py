#!/usr/bin/python3
"""Prime Game function"""


def is_prime(num):
    """Function to determine if num is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def can_win(nums):
    """Determine the winner of each round"""
    for n in nums:
        if is_prime(n):
            return "Maria"
    return "Ben"


def isWinner(x, nums):
    """Function returns winner that win most rounds"""
    maria_wins = 0
    ben_wins = 0

    if x < 1 or not nums:
        return None

    for n in nums:
        if is_prime(n):
            if n == 2:
                maria_wins += 1
            else:
                ben_wins += 1

    round_count = 0

    for n in nums:
        if is_prime(n):
            if n == 2:
                maria_wins += 1
            else:
                ben_wins += 1

        round_count += 1
        if round_count >= x:
            break

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    elif maria_wins == ben_wins:
        return None
    else:
        winner = can_win(nums)
        if winner == "Maria" or winner == "Ben":
            return winner
        else:
            return None
