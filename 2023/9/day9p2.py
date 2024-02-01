from pprint import pp

input_type = 'p'
input_types = {'v': 'test_vector', 'e': 'example_input', 'p': 'puzzle_input'}
ifilename = input_types[input_type]

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.readlines()
data = [i.strip() for i in data]
print(data)


class History:
    def __init__(self, line: str):
        self.hist_data = [int(i) for i in line.split()]
        self.hist_data.append('E')
        self.curr_sequence = self.hist_data
        self.sequences = [self.curr_sequence]

    def __repr__(self):
        return f"{self.sequences}"

    def calc_hist_sequences(self):
        next_sequence = self.calc_next_sequence()
        self.sequences.append(next_sequence)
        self.curr_sequence = next_sequence
        while not all([i == 0 for i in next_sequence[:-1]]):
            next_sequence = self.calc_next_sequence()
            self.sequences.append(next_sequence)
            self.curr_sequence = next_sequence

    def calc_next_sequence(self):
        next_sequence = []
        for i, d in enumerate(self.curr_sequence):
            if isinstance(self.curr_sequence[i+1], int):  # Kind of cheating by using an 'E' to find the end of the seq
                next_sequence.append(self.curr_sequence[i+1] - d)
            else:
                next_sequence.append('E')
                return next_sequence

    def reverse_all_sequences(self):
        reversed_sequences = []
        for s in self.sequences:
            s.pop()
            rev_seq = list(reversed(s))
            rev_seq.append('E')
            reversed_sequences.append(rev_seq)
        self.sequences = reversed_sequences

    def predict_next_value(self):
        next_value = 0
        for s in reversed(self.sequences):
            s[-1] = s[-2] - next_value
            next_value = s[-1]


print("\nCreate a History object for each line in the dataset:")
histories = []
for d in data:
    histories.append(History(d))
# pp(histories)

print("\nCreate the list of sequences for each history:")
for h in histories:
    h.calc_hist_sequences()
pp(histories)

print("\nReverse all sequences to make it easier to calculate the prev value:")
for h in histories:
    h.reverse_all_sequences()
pp(histories)

print("\nPredict the next value in the history sequence:")
for h in histories:
    h.predict_next_value()
pp(histories)

answer2 = 0
print("\nCalculate the final answer:")
for h in histories:
    answer2 += h.sequences[0][-1]
print(f"Answer to Part 2: {answer2}")
