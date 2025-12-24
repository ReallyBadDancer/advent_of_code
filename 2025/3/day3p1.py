EXAMPLE = False

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.readlines()
        data = [list(d.strip()) for d in data]
        # print(data)
        data = [list(map(int,d)) for d in data]

    joltages = []
    for d in data:
        first_dig = max(d)
        max_index = d.index(first_dig)
        if max_index == len(d)-1:
            second_dig = d.pop()
            first_dig = max(d)
        else:
            d = d[max_index+1:]
            # print(d)
            second_dig = max(d)

        print([first_dig,second_dig])
        joltages.append(10*first_dig+second_dig)
        print(sum(joltages))






