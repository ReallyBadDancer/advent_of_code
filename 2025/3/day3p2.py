EXAMPLE = True

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.readlines()
        data = [list(d.strip()) for d in data]
        data = [list(map(int,d)) for d in data]

    line_length = len(data[0])  # Length of each data line

    joltages = []
    for d in data:
        bank = []
        bank_length = 12

        while bank_length > 0:
            curr_dig = max(d)
            while True:
                curr_index = d.index(curr_dig)
                if len(d) - curr_index+1 > bank_length:
                    bank.append(curr_dig)
                    d = d[curr_index+1:]
                    bank_length -= 1
                    break
                else:
                    curr_dig -= 1
                    while curr_dig not in d:
                        curr_dig -= 1

        print(f"Added a bank: {bank}")
        bank = int("".join(map(str,bank)))
        joltages.append(bank)

    print(joltages)
    print(sum(joltages))