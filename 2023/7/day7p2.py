from pprint import pp

test = False
ifilename = "example_input" if test else "puzzle_input"

print("\nImport Raw data:")
# with open("test_vector") as ifile:
with open(ifilename) as ifile:
    data = ifile.read()
pp(data)

print("\nConvert to a list of list of hands and their wagers:")
data = [[line.split()[0], int(line.split()[1])] for line in data.splitlines()]
pp(data)

print("\nGenerate a dictionary mapping card power to card face")
card_faces = "AKQT98765432J"
card_strengths = range(1, 14)
card_power_dict = {face: strength for face, strength in zip(card_faces, card_strengths)}
print(card_power_dict)

print("\nConvert all cards to card power values.")
for inx, line in enumerate(data):
    power_list = []
    for c in data[inx][0]:
        power_list.append(card_power_dict[c])
    data[inx][0] = power_list
pp(data)

print("\nGenerate a dict of hand types and number ranks")
hand_types = ['HC', 'P', '2P', '3OK', 'FH', '4OK', '5OK']
hand_type_ranks = {t: r for t, r in zip(hand_types, range(1, 8))}
print(hand_type_ranks)


def get_hand_type(h: list) -> int:
    """
        Take in a hand (a list of numbers corresponding to the "power level" of each card) and assign it a type rank
        according to this scheme:
        High: 1, Pair: 2, Two Pair: 3, Three of a kind: 4, Full House: 5, Four of a kind: 6, Five of a kind: 7
        Probably need to make this recursive in order to be fancy.
        :param h: Five integer list representing the card hand in terms of card "power"
        :return: Rank of the hand type rank as an integer
        """

    counts = [h.count(i) for i in card_strengths]  # Get a count of each card within the hand to find pairs, etc
    if 5 in counts:  # 5 of a kind
        return 7
    if 4 in counts:  # 4 of a kind
        if counts[-1] == 1:  # Got a joker, it's 5 of a kind (5OK)
            return 7
        else:  # Four of a kind with no joker, 4 of a kind (4OK)
            return 6
    if 3 in counts:  # Could be 3OK, FH, 4OK, or 5OK
        if counts[-1] == 3:  # Got three jokers, gives 4 of a kind or 5 of a kind
            if 2 in counts:  # Got three jokers and 2 of something else, 5 of a kind.
                return 7
            else:  # Got 3 jokers and 2 mixed cards, four of a kind.
                return 6
        if counts[-1] == 2:  # Got 2 jokers and a 3 of a kind, makes 5 of a kind.
            return 7
        if counts[-1] == 1:  # 1 joker gives four of a kind with another 3 of a kind
            return 6
        if counts[-1] == 0:
            if 2 in counts:
                return 5  # Full house
            else:
                return 4  # 3 of a kind
        else:
            print("Error, invalid hand.")
            exit(1)
    if 2 in counts:  # Two pair or pair? Possible FH or 4OK with joker.
        if counts.count(2) == 2:  # Handle variations on two pair
            if counts[-1] == 1:
                return 5  # Full house with two pair and one joker
            elif counts[-1] == 2:
                return 6  # Four of a kind with one pair and two jokers
            else:
                return 3  # Just two pair with no jokers
        else:  # Handle single pair cases
            if counts[-1] == 2: # Single pair of jokers
                return 4  # Three of a kind
            if counts[-1] == 1: # Pair with a joker
                return 4  # Three of a kind
            if counts[-1] == 0:  # Pair with no joker
                return 2
    if counts[-1] == 1:  # At least we got a joker for the pair.
        # print(h, "1PJ")
        return 2
    return 1  # High Card


print("\n Append the hand rank to each [hand, wager] to get [hand, wager, rank] items in the dataset, then sort it")
for line in data:
    line: list
    line.append(get_hand_type(line[0]))  # Ok to modify in place since just adding another element to each hand list.

data = sorted(data, key=lambda hand_rank: hand_rank[2])  # Sort data by on the third element in each list.
# pp(data)

print("\nGroup together hands by hand rank:")
sorting_dict = {r: [] for r in range(1, 8)}
for k, v in sorting_dict.items():
    for h in data:
        if h[2] == k:
            v.append(h)
pp(sorting_dict)

print("\nOrder each hand rank from highest to lowest hand within that rank")
sorted_list = []
for rank, hands in sorting_dict.items():
    if hands:
        temp_hands = reversed(sorted(hands, key=lambda x: x[0]))
        for hand in temp_hands:
            sorted_list.append(hand)
pp(sorted_list)

print('\nCalculate answer for part 2')
answer2 = 0
for i, h in enumerate(sorted_list):
    answer2 += ((i+1) * h[1])
print(f"Part 2 Answer: {answer2}")
print("Part 2 Wrong Answer: 253716851")
print("Part 2 Right Answer: 253718286")
