import sys
import re
import string
from pprint import pprint

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

print("All dots removed:")
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
pprint(engine_part_numbers)


class EnginePart:
    def __init__(self, partno, rownum, colstart, schemrow, prevrow, nextrow):
        self.partno = partno
        self.partnum = int(partno)
        self.rownum = rownum
        self.colstart = colstart
        self.colend = self.colstart + len(partno) - 1
        self.schemrow = schemrow
        self.prevrow = prevrow
        self.nextrow = nextrow
        self.part = False

    def check_if_part(self) -> bool:
        # print(f"Checking part {self.partno}")
        if self.schemrow[self.colstart-1] != '.':
            self.part = True
            print(self.partno, " is valid")
            return True
        if self.schemrow[self.colend+1] != '.':
            self.part = True
            print(self.partno, " is valid")
            return True
        for col in self.prevrow[self.colstart-1:self.colend+2]:  # Look up
            print(f"Checking above row: {self.prevrow[self.colstart - 1:self.colend + 1]}")
            if col not in string.digits and col != '.':
                self.part = True
                print(self.partno, " is valid")
                return True
        for col in self.nextrow[self.colstart-1:self.colend+2]:  # Look down
            # print(f"Checking below row from index {self.colstart-1} to {self.colend+2} of {self.nextrow}: {self.nextrow[self.colstart-1:self.colend+1]}")
            if col not in string.digits and col != '.':
                self.part = True
                print(self.partno, " is valid")
                return True
        print(self.partno, " is not a valid part.\n-----")
        self.part = False
        return False

engine_parts = []
for row_num, partrow in enumerate(engine_part_numbers):
    if row_num in [0, len(engine_part_numbers)-1]:
        continue

    slice_inx = 0
    for part in partrow:
        # print("Creating part for item", part)
        curr_row = test_input[row_num]
        prev_row = test_input[row_num-1]
        next_row = test_input[row_num+1]
        part_start_inx = curr_row.find(part, slice_inx)
        slice_inx = part_start_inx+1
        engine_parts.append(EnginePart(part, row_num, part_start_inx, curr_row, prev_row, next_row))

answer1 = 0
for part in engine_parts:
    if part.check_if_part():
        print(f"Adding {part.partno} to {answer1}")
        answer1 += part.partnum
        print(f"Answer updated to {answer1}\n------")
print(answer1)


answer1 = 0
for part in engine_parts:
    if part.part:
        answer1 += part.partnum
print(answer1)




