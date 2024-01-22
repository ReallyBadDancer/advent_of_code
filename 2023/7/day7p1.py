from pprint import pp

test = True
ifilename = "example_input" if test else "puzzle_input"

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.read()
# print(data)

print("\nConvert to a list of list of hands and their wagers:")
data = [[line.split()[0], int(line.split()[1])] for line in data.splitlines()]
pp(data)

print("\nGenerate a dictionary mapping card power to card face")
card_faces = "AKQJT98765432"
card_strengths = range(1, 14)
card_power_dict = {face: strength for face, strength in zip(card_faces, card_strengths)}
print(card_power_dict)

print("\nConvert all cards to card power values and sort by power value")
for inx, line in enumerate(data):
    power_list = []
    for c in data[inx][0]:
        power_list.append(card_power_dict[c])
    power_list = sorted(power_list)
    data[inx][0] = power_list
pp(data)

print("\nGenerate a dict of hand types and number ranks")
hand_types = ['HC', 'P', '2P', '3OK', 'FH', '4OK', '5OK']
hand_type_ranks = {t: r for t, r in zip(hand_types, range(1,8))}
print(hand_type_ranks)


def get_hand_type(h: str) -> int:
    """
        Take in a hand and assign it a type rank according to this scheme:
        High: 1, Pair: 2, Two Pair: 3, Three of a kind: 4, Full House: 5, Four of a kind: 6, Five of a kind: 7
        Probably need to make this recursive in order to be fancy.
        :param h: Five character string representing the card hand
        :return: Rank of the hand type rank as an integer
        """

    # h = list(h)
    counts = [h.count(i) for i in card_strengths]

    for c in card_faces:
        # counts[i] = h.count(c)
        if 5 in counts:
            return 7
        if 4 in counts:
            return 6
        if 3 in counts:
            if 2 in counts:
                return 5
            else:
                return 4
        if 2 in counts:
            counts.remove(2)
            if 2 in counts:
                return 3
            else:
                return 2
    return 1


print("\n Append the hand rank to each [hand, wager] to get [hand, rank, wager] items in the dataset, then sort it")
for line in data:
    line.append(get_hand_type(line[0]))
    # print(line)

data = sorted(data, key=lambda hand_rank: hand_rank[2])
pp(data)

print("\n Group together hands by hand rank:")
sorting_dict = {r: [] for r in range(1, 8)}
for k, v in sorting_dict.items():
    for h in data:
        if h[2] == k:
            v.append(h)

pp(sorting_dict)

exit()
print("\nOrder each hand rank from highest to lowest hand within that rank")
for rank, hands in sorting_dict.items():
    for hand in hands:
        print(rank, hand)
