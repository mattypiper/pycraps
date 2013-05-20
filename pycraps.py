#!/usr/bin/env python

import random, sys

r = random.Random()

def dice():
    return r.randint(1,6) + r.randint(1,6)

def play():
    ret = []
    while True:
        roll = dice()
        ret.append(roll)
        if roll == 7:
            break
    return ret

numbers = [4,5,6,8,9,10]

def dontpass(rolls, stake=10, multiplier=3):
    win = [2,3]
    loss = [7,11]
    push = [12]
    
    wins = [x for x in rolls if x in win]
    losses = [x for x in rolls if x in loss]
    pushes = [x for x in rolls if x in push]

    for x in numbers:
        c = rolls.count(x)
        if c > 1:
            losses.extend([x] * (c-1))
        if c:
            wins.extend([x])

    # front line
    dollas = stake * (len(wins) - len(losses))

    # odds line
    for w in [x for x in wins if x in numbers]:
        odds_win = odds(w, stake, multiplier, False)
        dollas += odds_win
    for l in [x for x in losses if x in numbers]:
        odds_loss = stake * multiplier
        dollas -= odds_loss

    return dollas

def odds(r, stake, multiplier, rightway):
    if rightway: inv = 1
    else: inv = -1

    if r == 4 or r == 10:
        factor = 2 ** inv
    elif r == 5 or r == 9:
        factor = (3./2) ** inv
    elif r == 6 or r == 8:
        factor = (6./5) ** inv
    else:
        raise Exception("no odds for {}".format(r))
    return int(stake * multiplier * factor)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "{} <bankroll> <plays>".format(sys.argv[0])
        sys.exit(2)

    bank = int(sys.argv[1])
    plays = int(sys.argv[2])

    while plays:
        print "-" * 40
        plays -= 1
        a = play()
        print "{} rolls: {}".format(len(a), a)
        money = dontpass(a)
        print "${}".format(money)
        bank += money
        print "bankroll: ${}".format(bank)

    print "-" * 40

