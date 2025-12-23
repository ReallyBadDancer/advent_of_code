EXAMPLE_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

EXAMPLE = False
INPUT_FILE = "day1p1_input"


if __name__ == '__main__':
    if EXAMPLE:
        lr_directions = EXAMPLE_INPUT.splitlines()
        # print(lr_directions)
    else:
        with open(INPUT_FILE) as f:
            lr_directions = f.read().splitlines()

    directions = []
    for item in lr_directions:
        if item[0] == "L":
            directions.append(int(item[1:])*(-1))
        else:
            directions.append(int(item[1:]))
    # print(directions)

    curr_pos = 50
    password = 0
    for direction in directions:
        curr_pos += direction
        # print("No modulo",  curr_pos)
        curr_pos %= 100
        # print(curr_pos)
        if curr_pos == 0:
            password += 1

    print("Part 1 Password is", password)

    curr_pos = 50
    password = 0
    pos_tuples = []
    for direction in directions:
        # print(f"Move from {curr_pos}: {direction}")
        dir_tuple = divmod(curr_pos+direction, 100)
        clicks = abs(dir_tuple[0])
        curr_pos = (curr_pos + direction) % 100
        # print("Quotient and Remainder: ", dir_tuple, "Position: ", curr_pos)
        # print("CLICKS:", clicks)
        password += clicks

    print("Part 2 Password: ", password)
