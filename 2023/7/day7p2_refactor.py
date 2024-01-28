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


class Play:

    # Define card order and strengths
    card_faces = "AKQT98765432J"
    card_strengths = range(1, 14)
    card_power_dict = {face: strength for face, strength in zip(card_faces, card_strengths)}

    # Generate a dict of hand types and number ranks
    hand_types = ['HC', 'P', '2P', '3OK', 'FH', '4OK', '5OK']
    hand_type_ranks = {r: t for t, r in zip(hand_types, range(1, 8))}

    def __init__(self, p: list):
        p: list[str, int]
        self.hand = p[0]
        self.powers = [self.card_power_dict[f] for f in self.hand]
        self.wager = p[1]
        self.counts = [self.hand.count(i) for i in self.card_faces]
        self.hand_type = self.convert_jokers_and_get_hand_type()

    def __repr__(self):
        return (f"Hand: {self.hand}, Powers: {self.powers}\n"
                f"Counts: {self.counts}, Wager: {self.wager}, Type: {self.hand_type_ranks[self.hand_type]}")

    def get_hand_type(self):
        """
                Take in a hand (a list of numbers corresponding to the "power level" of each card) and assign it a type rank
                according to this scheme:
                High: 1, Pair: 2, Two Pair: 3, Three of a kind: 4, Full House: 5, Four of a kind: 6, Five of a kind: 7
                Probably need to make this recursive in order to be fancy.
                :param h: Five integer list representing the card hand in terms of card "power"
                :return: Rank of the hand type rank as an integer
                """

        if 5 in self.counts:  # 5 of a kind
            return 7
        if 4 in self.counts:  # 4 of a kind
            return 6
        if 3 in self.counts:  # 3 of a kind or full house?
            if 2 in self.counts:
                return 5  # Full house
            else:
                return 4  # 3 of a kind
        if 2 in self.counts:  # Two pair or pair?
            if self.counts.count(2) == 2:
                return 3  # Two pair
            else:
                return 2  # Just one pair
        return 1  # High Card

    def convert_jokers_and_get_hand_type(self):
        if 'J' in self.hand:
            print(self.hand)
            num_jokers = self.counts.pop()
            if num_jokers == 5:
                return 7
            most_cards = max(self.counts)
            most_cards_index = self.counts.index(most_cards)
            self.counts[most_cards_index] += num_jokers

            return self.get_hand_type()
        else:
            return self.get_hand_type()



plays = []
for line in data:
    plays.append(Play(line))






# print("\n Append the hand rank to each [hand, wager] to get [hand, wager, rank] items in the dataset, then sort it")
# for line in data:
#     line: list
#     line.append(get_hand_type(line[0]))  # Ok to modify in place since just adding another element to each hand list.
#
# data = sorted(data, key=lambda hand_rank: hand_rank[2])  # Sort data by on the third element in each list.
# # pp(data)

print("\nGroup together hands by hand rank:")
sorting_dict = {r: [] for r in range(1, 8)}
for k, v in sorting_dict.items():
    for play in plays:
        if play.hand_type == k:
            v.append(play)
pp(sorting_dict)

print("\nOrder each hand rank from highest to lowest hand within that rank")
sorted_list = []
for rank, plays in sorting_dict.items():
    if plays:
        temp_plays = sorted(plays, key=lambda x: x.powers, reverse=True)
        for play in temp_plays:
            sorted_list.append(play)
pp(sorted_list)

print('\nCalculate answer for part 2')
answer2 = 0
for i, h in enumerate(sorted_list, 1):
    answer2 += (i * h.wager)
print(f"Part 2 Answer: {answer2}")
print("Part 2 Wrong Answer: 253716851")
print("Part 2 Right Answer: 253718286")
