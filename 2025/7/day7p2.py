# Second attempt at day 7 part 2. Went to reddit for a hint: https://www.reddit.com/r/adventofcode/comments/1pgb377/2025_day_7_part_2_hint/
# The hint made it really trivial. 
from pprint import pprint

EXAMPLE = True

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.read().splitlines()

    # Convert all dots into zeroes to track timelines. 
    data = [list(i) for i in data]
    for row in data:
        for inx, col in enumerate(row):
            if col == '.':
                row[inx] = 0

    print("Data: ")
    pprint(data)

    for row_inx in range(len(data)):
        for col_inx, c in enumerate(data[row_inx]):
            if c == 'S':
                data[row_inx+1][col_inx] += 1
            elif c == '^':  # Handle splitters in current row.
                data[row_inx][col_inx-1] += data[row_inx-1][col_inx]
                data[row_inx][col_inx+1] += data[row_inx-1][col_inx]
            elif type(c) == int:  # Handle propagating beams above current row.
                if type(data[row_inx-1][col_inx]) == int:  # Don't try to propagate carets or S.
                    data[row_inx][col_inx] += data[row_inx-1][col_inx]

    print(sum(data[-1]))  # Total timelines is the sum of the final row. 