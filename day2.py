from utils import file_to_lines

sign_normalizations = {"X": "A", "Y": "B", "Z": "C"}
sign_scores = {"A": 1, "B": 2, "C": 3}
rules_to_win = {"A": "C", "B": "A", "C": "B"}  # a beats c, etc..
rules_to_loose = {"C": "A", "A": "B", "B": "C"}  # c is beaten by a, etc...


def calc_round_score(me, op):
    draw = op == me
    i_won = rules_to_win[me] == op
    extra_points = 6 if i_won else 3 if draw else 0
    return sign_scores[me] + extra_points


def solve(rounds):
    score = 0
    for round in rounds:
        opponent, mission = (
            sign_normalizations.get(sign, sign)
            for sign in round.strip().split(" ")
        )
        if mission == "A":
            me = rules_to_win[opponent]
        elif mission == "C":
            me = rules_to_loose[opponent]
        else:
            me = opponent
        score += calc_round_score(me, opponent)
    return score


if __name__ == "__main__":
    print(solve(file_to_lines(day=2)))
