import random

moves = {}
counter_move = {"R": "P", "P": "S", "S": "R"}


def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    guess = "R"
    PATTERNS = 6

    if len(opponent_history) > PATTERNS:
        pattern = "".join(opponent_history[-PATTERNS:])

        if "".join(opponent_history[-(PATTERNS + 1) :]) in moves.keys():
            moves["".join(opponent_history[-(PATTERNS + 1) :])] += 1
        else:
            moves["".join(opponent_history[-(PATTERNS + 1) :])] = 1

        next_moves = [pattern + "R", pattern + "P", pattern + "S"]

        for i in next_moves:
            if not i in moves.keys():
                moves[i] = 0

        next_move = max(next_moves, key=lambda key: moves[key])

        if next_move[-1] == "P":
            guess = "S"
        if next_move[-1] == "R":
            guess = "P"
        if next_move[-1] == "S":
            guess = "R"

    return guess
