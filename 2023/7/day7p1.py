test = True
ifilename = "example_input" if test else "puzzle_input"

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.read()
print(data)

print("\nConvert to a list of tuple of hands and their wagers:")
data = [(line.split()[0], int(line.split()[1])) for line in data.splitlines()]
print(data)

print("\nGenerate a dictionary mapping card power to card face")
card_faces = "AKQJT98765432"
card_strengths = range(14, 1, -1)
card_power_dict = {face: strength for face, strength in zip(card_faces, card_strengths)}
print(card_power_dict)

for hand, wager in data:
    temp_hand = list(hand)
    cards = []
    while temp_hand:
        card = temp_hand.pop()
        # IF this card is in the rest of the hand
        #   THEN IF this card is in the rest of the hand,
        #       THEN get the count and add it to cards, and remove the rest of the instances of this card
        #

