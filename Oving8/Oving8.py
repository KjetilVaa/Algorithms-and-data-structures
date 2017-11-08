from sys import stdin
import bisect
Inf = 1000000000


def min_coins_greedy(coins, value):
    spent = 0
    while value != 0:
        for i in coins:
            if value >= i:
                value -= i
                spent += 1
                break
    return spent


def min_coins_dynamic(coins, value):
    log = [0]
    def iterate(coins,value):
        local = []
        for i in coins:
            if i > value:
                break
            local.append(log[value-i]+1)
        log.append(min(local))

    for i in range(1,value+1):
        iterate(coins,i)
    return log[-1]






def can_use_greedy(coins):
    """for cur,next in zip(coins[:-1],coins[1:]):
        if next%cur != 0:
            return False
    return True"""



coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    coins.reverse()
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))
