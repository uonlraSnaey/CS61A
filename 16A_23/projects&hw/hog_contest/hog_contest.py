def final_strategy(score, opponent_score, cutoff=5, num_rolls=6):
    if is swap(score+1, opponent_score) and opponent_score - score >= cutoff:
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

