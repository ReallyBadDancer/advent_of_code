import sys
import re
import string
from pprint import pprint
from engine_part import EnginePart

test = True
ifilename = "example_input" if test else "puzzle_input"

with open(ifilename) as ifile:
    test_input = ifile.read().splitlines()

print("Test Input: ")
# pprint(test_input)

print("Test Input but with '.' padding: ")
temp_input = []
for line in test_input:
    temp_input.append('.' + line + '.')
extra_line = '.'*len(temp_input[0])  # Create a line of dots to add to first and last rows.
temp_input.insert(0,extra_line)
temp_input.append(extra_line)
test_input = temp_input
pprint(test_input)

# digits = string.digits  # Going to use this to check for if something is a digit later.

print("All dots and symbols removed:")
engine_part_numbers = []
for row in test_input:
    engine_part_numbers.append(re.split(r'\D+', row))
    # engine_part_numbers.append(row.split('.'))
# pprint(engine_part_numbers)

# print("Other characters removed:")
# for row in engine_part_numbers:
#     for inx, entry in enumerate(row):
#         row[inx] = ''.join(filter(str.isdecimal, entry))
# pprint(engine_part_numbers)

print("Empty space removed:")
for row in engine_part_numbers:
    try:
        while(True):
            row.remove('')
    except ValueError:
        pass
# pprint(engine_part_numbers)

engine_parts = []
for row_num, partrow in enumerate(engine_part_numbers):
    if row_num in [0, len(engine_part_numbers)-1]:
        continue

    slice_inx = 0
    for part in partrow:
        # print(f"Processing part {part}")
        curr_row = test_input[row_num]
        prev_row = test_input[row_num-1]
        next_row = test_input[row_num+1]
        part_start_inx = curr_row.find(part, slice_inx)
        slice_inx = part_start_inx + len(part)
        engine_parts.append(EnginePart(part, row_num, part_start_inx, curr_row, prev_row, next_row))

answer1 = 0  # Calculate final answer for part 1.
for part in engine_parts:
    if part.check_if_part():
        answer1 += part.partnum
print("Answer for Part 1: ", answer1)
print("-----\nBegin part 2:\n-----")


class Gear:

    # Regular expressions used to count up how many parts.
    double_part_rex = r"\d\D\d"
    single_part_rex = r"\d+|\D+\d+|\d+\D+"

    def __init__(self, rownum, col, schemrow, prevrow, nextrow):
        print("Making a gear!")
        self.rownum = rownum
        self.col = col
        self.schemrow = schemrow
        self.prevrow = prevrow
        self.nextrow = nextrow
        self.gear = False
        self.gear_ratio_values = 0

    def check_if_gear(self):
        print("Checking if it's a real gear...")
        num_adjacent = 0
        # Check left and right, and add to total adjacent numbers if number found.
        print("Checking left/right: ", self.schemrow[self.col - 1], '*', self.schemrow[self.col + 1])
        for col in [self.schemrow[self.col-1], self.schemrow[self.col+1]]:
            if col in string.digits:
                print("Adding 1 part for left/right")
                num_adjacent += 1
        # Check prev and next rows for how many adjacent parts
        prevrow_slice = self.prevrow[self.col-1:self.col+2]
        nextrow_slice = self.nextrow[self.col-1:self.col+2]
        for slice in [prevrow_slice, nextrow_slice]:
            print("Checking above/below slice: ", slice)
            if re.match(self.double_part_rex, slice):
                print("Adding 2 parts for above/below")
                num_adjacent += 2
            elif re.match(self.single_part_rex, slice):
                print("Adding 1 part above/below")
                num_adjacent += 1
        if num_adjacent == 2:
            self.gear = True
            print("It's a gear!")
            self.get_gear_ratio_values()
            return True
        else:
            self.gear = False
            print("Not a gear!")
            return False

    def get_gear_ratio_values(self):
        pass


gears = []
for row_inx, row in enumerate(test_input):
    for col_inx, col in enumerate(row):
        if col == '*':
            gears.append(Gear(row_inx, col_inx, row, test_input[row_inx-1], test_input[row_inx+1]))

for gear in gears:
    gear.check_if_gear()
