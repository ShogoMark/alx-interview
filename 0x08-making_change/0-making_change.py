#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """function that accepts no of coins&total"""
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coin_sum = 0
    coin_count = 0

    for coin in sorted_coins:
        while coin_sum + coin <= total:
            coin_sum += coin
            coin_count += 1
    
    if coin_sum == total:
        return coin_count
    else:
        return -1
