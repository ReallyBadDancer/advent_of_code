from pprint import pprint
from card import Card

test = False
part_one = False
ifilename = "example_input" if test else "puzzle_input"

with open(ifilename) as ifile:
    data = ifile.read().splitlines()

# print("Split off Card Numbers")
data = [i.split(': ') for i in data]
# pprint(data)

# print('Get rid of "Card" and save card number as an integer')
temp_data = []
for card in data:
    temp_data.append([int(card[0].split('Card ')[1]), card[1]])
data = temp_data
# pprint(data)

# print("Split off the winners from the numbers we have")
temp_data = []
for card in data:
    temp_data.append([card[0], card[1].split(" | ")])
data = temp_data
# pprint(data)

# print("Get the winners and numbers we have (NWH) as lists")
temp_data = []
for card in data:
    temp_data.append([card[0], [i.split(" ") for i in card[1]]])
data = temp_data
# pprint(data)

# print("Remove extra whitespace")
temp_data = []
for inx, card in enumerate(data):
    card[1] = [list(filter(None, i)) for i in card[1]]
    temp_data.append([card[0], [[int(x) for x in inner_list] for inner_list in card[1]]])
data = temp_data
# pprint(data)

if part_one:
    print("Getting answer for part one:")
    deck = []
    for card in data:
        deck.append(Card(card, None))

    answer1 = 0
    for card in deck:
        answer1 += card.calculate_card_score()

    print("Final Answer for Part 1: ", answer1)
else:
    deck = {}
    print("Creating cards for pile in part 2:")
    for inx, card in enumerate(data):
        new_card = Card(card, data[inx+1:])
        deck.update({new_card.card_no: new_card})

    pprint(deck)
    print("Total cards: ", len(deck))


    for num, card in reversed(deck.items()):
        print(f"----\nGetting card numbers for {num}...")
        # Add this card to the pile
        if card.card_score != 0:
            for below_card in range(num+1, num+card.card_score+1):
                print(f"Adding pile from card {below_card} with pile size {deck[below_card].pile_size}")
                card.pile_size += deck[below_card].pile_size
        print(f"Final pile size for card {num} is {card.pile_size}")

    print("\nAdd up pile sizes for call cards in the deck:")
    total_card_pile = 0
    for num, card in deck.items():
        print(f"Adding pile of {card.pile_size} from card {num}")
        total_card_pile += card.pile_size

    print(f"Total cards in pile: {total_card_pile}")
