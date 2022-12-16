with open("example_input.txt") as infile:
    data = infile.read().split('\n')

instructions = [i.split(' ') for i in data]


def head_step(curr_loc: list, instruction: list) -> list:
    new_loc = curr_loc.copy()
    direction = instruction[0]
    distance = int(instruction[1])
    if direction == 'R':
        new_loc[0] = curr_loc[0] + distance
    elif direction == 'L':
        new_loc[0] = curr_loc[0] - distance
    elif direction == 'U':
        new_loc[1] = curr_loc[1] + distance
    elif direction == 'D':
        new_loc[1] = curr_loc[1] - distance
    else:
        print("Something went wrong")

    return new_loc


def tail_step(head_loc: list, tail_loc: list, instruction: list) -> list:

    if abs(head_loc[0] - tail_loc[0]) <= 1 >= abs(head_loc[1] - tail_loc[1]):
        return tail_loc
    elif abs(head_loc[0] - tail_loc[0]) > 1 and head_loc[1] == tail_loc[1]:
        # This is supposed to move the tail one step in the direction of the head in the x-axis
        return [head_step(tail_loc, instruction)[0], tail_loc[1]]
    elif abs(head_loc[1] - tail_loc[1]) > 1 and head_loc[0] == tail_loc[0]:
        # This is supposed to move the tail one step in the direction of the head in the y-axis
        return [tail_loc[0], head_step(tail_loc, instruction)[1]]


# History of the [x, y] coordinates of the head and tail of the rope.
head_history = [[0, 0]]
tail_history = [[0, 0]]
for step in instructions:
    head_history.append(head_step(head_history[-1], step))
    tail_history.append(tail_step(head_history[-1], tail_history[-1], step))
