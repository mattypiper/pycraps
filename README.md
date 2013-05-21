pycraps
=======

Simple craps simulator implemented in python. Only care about pass and don't pass line and associated odds.

Currently only don't pass is implemented, so all sims will use a don't pass strategy.

Sample runs:

1. Run 1 trial showing details of the roll and win/loss figure for each point.
 * $200 starting bankroll
 * playing until 4 points have won
<pre>
    $ pycraps.py 200 4
    ----------------------------------------
    8 rolls: [6, 11, 9, 8, 8, 5, 5, 7]
    $30
    bankroll: $230
    ----------------------------------------
    2 rolls: [3, 7]
    $0
    bankroll: $230
    ----------------------------------------
    6 rolls: [3, 9, 5, 6, 9, 7]
    $55
    bankroll: $285
    ----------------------------------------
    3 rolls: [5, 10, 7]
    $45
    bankroll: $330
    ----------------------------------------
</pre>

2. Run 100,000 trials with each trial having:
 * $500 starting bankroll
 * playing until 10 points have won
<pre>
    $ pycraps.py 500 10 --trials 100000 --stats --silent
    mean   = 491.013
    stddev = 297.383
    min = -1845
    max = 1365
    average risked = 1800.5417
    total risked = 180054170
    house = -0.005
</pre>