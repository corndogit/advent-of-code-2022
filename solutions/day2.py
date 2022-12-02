# 1 = rock, 2 = paper, 3 = scissors
hands = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}


def calc_round_score(picks, part2=False):
    """
    Determines the winner of a round. picks[0] = elf and picks[1] = player.
    :param picks: Hands chosen for the round
    :param part2: Whether to run for the solution of part 2
    :return: value of the score for the round
    """
    opponent_choice = hands[picks[0]]
    player_choice = hands[picks[1]]

    # PART 2 ONLY: X = lose, Y = tie, Z = win
    if part2:
        if picks[1] == 'X':
            player_choice = opponent_choice - 1 if opponent_choice != 1 else 3  # force a loss
        elif picks[1] == 'Z':
            player_choice = opponent_choice + 1 if opponent_choice != 3 else 1  # force a win
        else:
            player_choice = hands[picks[0]]  # choose same hand to force a tie

    # add points for whichever hand the player picked
    outcome = player_choice

    # determine if any points are added for winning
    if opponent_choice == player_choice:
        outcome += 3  # result is a tie
    else:
        if opponent_choice == 3:
            if player_choice == 1:
                outcome += 6  # player wins with rock
        else:
            if player_choice == opponent_choice + 1:
                outcome += 6  # player wins with paper or scissors

    return outcome


if __name__ == "__main__":
    with open("../inputs/day2.txt") as file:
        rounds = [r.strip('\n').split(' ') for r in file.readlines()]

    print("Part 1:", sum(map(calc_round_score, rounds)))
    print("Part 2:", sum(map(lambda r: calc_round_score(r, True), rounds)))
