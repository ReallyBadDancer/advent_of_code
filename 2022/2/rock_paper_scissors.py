
def process_puzzle_input():
    opp_plays = {'A': 1, 'B': 2, 'C': 3}
    my_plays = {'X': 1, 'Y': 2, 'Z': 3}
    with open("puzzle_input_02.txt", mode='r') as ifile:
        matchup_list = ifile.read().split('\n')

    print(matchup_list)
    matchup_list = [i.split(' ') for i in matchup_list]
    print(matchup_list)
    matchup_list = [[opp_plays[i[0]], my_plays[i[1]]] for i in matchup_list]
    print(matchup_list)
    return matchup_list


def decide_win_loss_shape(opp_shape: str, desired_result: str) -> str:
    if opp_shape == 'A':
        if desired_result == 'X':
            return 'Z'
        else:
            return 'Y'
    elif opp_shape == 'B':
        if desired_result == 'X':
            return 'X'
        else:
            return 'Z'
    elif opp_shape == 'C':
        if desired_result == 'X':
            return 'Y'
        else:
            return 'A'


def main():

    print("Starting Phase 1:")

    # Example Input:
    # matchup_list = "A Y\nB X\nC Z"
    # matchup_list = matchup_list.split('\n')

    matchup_list = process_puzzle_input()

    numeric_wins = [[1, 2], [2, 3], [3, 1]]
    numeric_losses = [[2, 1], [3, 2], [1, 3]]

    score = 0
    for matchup in matchup_list:
        score += matchup[1]

        if matchup[0] == matchup[1]:
            score += 3
        elif matchup in numeric_wins:
            score += 6
        elif matchup in numeric_losses:
            score += 0
        else:
            print("You done messed up.")

    print(f"Final phase 1 score is: {score}")
    print("Starting phase 2:")

    # Part 2:
    with open("puzzle_input_02.txt", mode='r') as ifile:
        matchup_list = ifile.read().split('\n')
        print(matchup_list)
        matchup_list = [i.split(' ') for i in matchup_list]
        print(matchup_list)

    # Test Input:
    matchup_list = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
    shape_values = {'A': 1, 'X': 1, 'B': 2, 'Y':2, 'C': 3, 'Z': 3}

    score = 0
    for matchup in matchup_list:
        if matchup[1] == 'Y':  # Draw: Just use opponent's shape for the shape value and add 3 for the win.
            score += shape_values[matchup[0]] + 3
        elif matchup[1] == 'X':  # Lose: Decide which shape to use for the shape score and add 0 for the loss.
            shape = decide_win_loss_shape(matchup[0], matchup[1])
            score += shape_values[shape]
        elif matchup[1] == 'Z':  # Win: Decide which shape to use for the shape score and add 6 for that sweet win.
            shape = decide_win_loss_shape(matchup[0], matchup[1])
            score += shape_values[shape] + 6

    print(f"Final phase 2 score is: {score}")


if __name__ == "__main__":
    main()
