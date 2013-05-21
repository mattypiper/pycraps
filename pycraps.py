#!/usr/bin/env python

import random, sys, argparse, numpy

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
    risk = stake * len(rolls)

    # odds line
    for w in [x for x in wins if x in numbers]:
        odds_win = odds(w, stake, multiplier, False)
        dollas += odds_win
        risk += stake * multiplier
    for l in [x for x in losses if x in numbers]:
        odds_loss = stake * multiplier
        dollas -= odds_loss
        risk += odds_loss
     
    return (risk, dollas)

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

def main():
    parser = argparse.ArgumentParser(description = 'Craps simulator')
    parser.add_argument('bankroll', type=int, help='starting bankroll')
    parser.add_argument('N', type=int, default=10, help='number of points to simulate')
    parser.add_argument('--trials', type=int, default=1, help='number of trials (ie casino visits)')
    parser.add_argument('-c', '--csv', action='store_true', help='output in csv format')
    parser.add_argument('--silent' , action='store_true', default=False, help='silent output')
    parser.add_argument('--stats' , action='store_true', default=False, help='calculate statistics for trials')
    
    args = parser.parse_args()
    
    csv = args.csv
    N = args.N
    trials = args.trials
    silent = args.silent
    stats = args.stats
    initial_bankroll = args.bankroll
    
    # store results in arrays for statistics
    results = []
    risked = []
    
    while trials:
        trials -= 1
        trial_risk = 0
        
        # reset trial variables
        bankroll = initial_bankroll
        N = args.N
        
        while N :
            N -= 1
            a = play()
            (risk, reward) = dontpass(a)
            
            trial_risk += risk
            bankroll += reward
            
            if not csv and not silent:
                print "-" * 40
                print "{} rolls: {}".format(len(a), a)
                print "${}".format(reward)
                print "bankroll: ${}".format(bankroll)

        if not csv and not silent:
            print "-" * 40
            
        if csv and not silent:
            print bankroll
        
        results.append(bankroll)
        risked.append(trial_risk)
            
    if stats:
        bankroll_array = numpy.array(results)
        risked_array = numpy.array(risked)
        
        avg_bankroll_result = numpy.mean(bankroll_array)
        bankroll_stddev = numpy.std(bankroll_array)
        print "mean   = {:.03f}".format(avg_bankroll_result)
        print "stddev = {:.03f}".format(bankroll_stddev)
        print "min = {}".format(numpy.min(bankroll_array))
        print "max = {}".format(numpy.max(bankroll_array))
        
        avg_risked = numpy.mean(risked_array)
        total_risked = numpy.sum(risked_array)
        
        print "average risked = {}".format(avg_risked)
        print "total risked = {}".format(total_risked)
        print "house = {:.03f}".format((avg_bankroll_result - initial_bankroll) / avg_risked)

if __name__ == "__main__":
    main()

