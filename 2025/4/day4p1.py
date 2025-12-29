EXAMPLE = False

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.readlines()
        data = [list(d.strip()) for d in data]
        print(data)


    accessible_rolls = 0
    rows = len(data)
    cols = len(data[0])

    for r in range(rows):
        for c in range(cols):
            # Create a window around the roll of interest to count the surrounding rolls.
            if data[r][c] == '@':
                r0 = max(0, r - 1)  # Min row index
                r1 = min(rows - 1, r + 1)  # Max row index
                c0 = max(0, c - 1)  # Min col index
                c1 = min(cols - 1, c + 1)  # Max col index

                surroundings = []
                for i in data[r0:r1+1]:  # Get rows inclusive of max index
                    surroundings= surroundings + i[c0:c1+1]  # Get cols inclusive of max index
                    print("Number of surrounding rolls: ", surroundings.count('@'))
                print(surroundings)
                if surroundings.count('@') < 5:
                    accessible_rolls += 1

    print(accessible_rolls)


