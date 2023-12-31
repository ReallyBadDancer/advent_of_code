class Card:
    def __init__(self, scratch_card, deck_slice):

        self.deck_slice = deck_slice
        self.card_no = scratch_card[0]
        self.winners = scratch_card[1][0]
        self.our_numbers_list = scratch_card[1][1]
        self.our_numbers = set(self.our_numbers_list)
        self.card_score = 0
        self.pile_size = 1
        for num in self.our_numbers_list:
            if num in self.winners:
                self.card_score += 1
        print(f"Created card {self.card_no} with {self.card_score} winners")

    def calculate_card_score(self):
        print("Calculating score for card ", self.card_no)
        for num in self.our_numbers:
            if num in self.winners:
                self.card_score = 1 if self.card_score == 0 else (self.card_score * 2)
        return self.card_score
