import sys
from parse import parse
from collections import deque

# with open("example_input.txt") as infile:
with open("puzzle_input.txt") as infile:
    data = infile.read().split('\n')

instructions = []
for ins in data:
    if parse("{} {}", ins):
        temp_ins = list(parse("{} {}", ins))
        temp_ins[1] = int(temp_ins[1])
        instructions.append(temp_ins)
    else:
        instructions.append(ins)

x_history = [1]
for item in instructions:
    x_history.append(x_history[-1])
    if item == 'noop':
        continue
    else:
        x_history.append(item[1]+x_history[-1])

interesting_values = [20, 60, 100, 140, 180, 220]
signal_strengths = []
for inx, val in enumerate(x_history):
    if inx+1 in interesting_values:
        print(inx+1, val, (inx+1)*val)
        signal_strengths.append((inx+1)*val)

print(f"The sum of signal strengths is: {sum(signal_strengths)}")
