

def main():
    opp_plays = {'A': 1, 'B': 2, 'C': 3}
    my_plays = {'X': 1, 'Y': 2, 'Z': 3}

    final_scores = {'Loss': 0, 'Draw': 3, 'Win': 8}

    # Example:
    # matchup_list = "A Y\nB X\nC Z"
    # matchup_list = matchup_list.split('\n')

    with open("puzzle_input_02.txt", mode='r') as ifile:
        matchup_list = ifile.read().split('\n')

    print(matchup_list)
    matchup_list = [i.split(' ') for i in matchup_list]
    print(matchup_list)
    matchup_list = [[opp_plays[i[0]], my_plays[i[1]]] for i in matchup_list]
    print(matchup_list)

    alpha_wins = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
    numeric_wins = [[1, 2], [2, 3], [3, 1]]
    alpha_losses = [['B', 'X'], ['C', 'Y'], ['A', 'Z']]
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




    # X = Lose
    # Y = Draw
    # Z = Win

if __name__ == "__main__":
    main()
