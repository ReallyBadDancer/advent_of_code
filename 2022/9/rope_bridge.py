with open("example_input.txt") as infile:
    data = infile.read().split('\n')

instructions = [i.split(' ') for i in data]


def head_step(curr_loc:list, instruction:list) -> list:
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


head_history = [[0, 0]]
tail_history = [[0, 0]]
for step in instructions:
    head_history.append(head_step(head_history[-1], step))



