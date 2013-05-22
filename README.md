pycraps
=======

Simple craps simulator implemented in python. Only care about pass and don't pass line and associated odds.

Defaults to pass line. Specify --dontpass to simulate a don't pass strategy.

<pre>usage: pycraps.py [-h] [--dontpass] [--trials TRIALS] [-c] [--silent] [--stats] bankroll N</pre>

Sample runs:

1. Run 1 trial showing details of the roll and win/loss figure for each point.
 * $1000 starting bankroll
 * playing pass line until 3 points have won
<pre>
$ pycraps.py 1000 3
----------------------------------------
18 rolls: [10, 6, 2, 8, 10, 8, 6, 4, 9, 8, 9, 3, 6, 2, 10, 11, 9, 7]
outcome: $224
risked: $570
bankroll: $1224
----------------------------------------
10 rolls: [8, 8, 9, 8, 4, 11, 9, 9, 6, 7]
outcome: $62
risked: $340
bankroll: $1286
----------------------------------------
6 rolls: [5, 9, 6, 10, 2, 7]
outcome: $-160
risked: $180
bankroll: $1126
----------------------------------------
</pre>

1. Run a trial, same as before, but play the don't pass line instead.
<pre>
$ pycraps.py 1000 3 --dontpass
----------------------------------------
4 rolls: [5, 9, 9, 7]
outcome: $10
risked: $130
bankroll: $1010
----------------------------------------
2 rolls: [4, 7]
outcome: $15
risked: $50
bankroll: $1025
----------------------------------------
3 rolls: [2, 2, 7]
outcome: $10
risked: $30
bankroll: $1035
</pre>

1. Run 100,000 trials with each trial having:
 * $1000 starting bankroll
 * playing pass line until 10 points have won
<pre>
$ pycraps.py 1000 10 --trials 100000 --stats --silent
mean   = 993.265
stddev = 402.384
min = -314
max = 4860
average risked = 1800.8993
total risked = 180089930
house = -0.374%
</pre>

1. Run 100,000 trials with each trial having:
 * $1000 starting bankroll
 * playing don't pass line until 10 points have won (lost from shooter's point of view)
<pre>
$ pycraps.py 1000 10 --trials 100000 --stats --silent --dontpass
mean   = 993.102
stddev = 297.702
min = -2015
max = 1745
average risked = 1799.3757
total risked = 179937570
house = -0.383%
</pre>