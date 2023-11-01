"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""
import sys
PLAYER_NAME = 'Jone'  # Change this line!
sys.path.append('/hog')
from hog import


def final_strategy(score, opponent_score):
    if is_swap(score + 1, opponent_score) and opponent_score - score >= cutoff:
        return 0

    fb = free_bacon(opponent_score)
    if is_swap(score + fb, opponent_score):
        if opponent_score <= score + fb:
            return num_rolls
        else:
            if opponent_score - score - fb < cutoff:
                return num_rolls
            else:
                return 0

    else:
        if fb >= cutoff:
            return 0
        else:
            return num_rolls