from parse import parse

# with open('example_input.txt', mode='r') as infile:
with open('puzzle_input.txt', mode='r') as infile:
    data = infile.read().split('\n')

# stack_count = 3
stack_count = 9

# Simple array of stack indices (i.e. where each crate will be.) Mainly for readability.
stack_indices = [i for i in range(0, 40, 4)]
print(stack_indices)

# Create empty stack columns
stack_columns = [[] for i in range(stack_count)]

# Build up the stacks for easy processing:
for line in data:
    if '1' in line:
        break  # End of starting stack state.
    for inx, letter in enumerate(line):
        if inx in stack_indices:
            if letter == ' ':
                continue  # No crate here.
            elif letter == '[':
                letter = line[inx+1]
                stack_index = int(inx/4)
                # print(f"Box! {stack_index+1},{letter}")
                stack_columns[stack_index].append(letter)
            else:
                print('Something went wrong.')

for col in stack_columns:
    col.reverse()
print(stack_columns)

# Get the instructions for pop/append operations.
instructions = []
for line in data:
    if not line or line[0] != 'm':
        continue
    else:
        instructions.append(list(parse('move {} from {} to {}', line)))

# Convert it all to integers and offset starting inx to zero for ease of use with python.
instructions = [[int(i)-1 for i in j] for j in instructions]
# Still need the correct # of crates per command.
for command in instructions:
    command[0] = command[0]+1
print(instructions)

part_one = False

# Part 1 Solution:
# ----------------
# Rearrange the creates in order by command by popping off the first col and then appending.
if part_one:
    for command in instructions:
        for crate in range(command[0]):
            temp = stack_columns[command[1]].pop()
            stack_columns[command[2]].append(temp)
    print(stack_columns)
# Get the top crate on each stack
    for col in stack_columns:
        print(col[-1])

# Part 2 Solution:
# Similar to part 1, but instead of moving the crates one at a time, accumulate them to a
# temporary list, reverse, then unpack.
# ----------------

for command in instructions:
    temp = []
    for crate in range(command[0]):
        temp.append(stack_columns[command[1]].pop())
    temp.reverse()
    print(temp)
    for item in temp:
        stack_columns[command[2]].append(item)
print(stack_columns)
for col in stack_columns:
    print(col[-1])
