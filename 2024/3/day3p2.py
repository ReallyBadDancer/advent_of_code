import numpy as np

import aoc_utils
import re


def get_start_stop_inx(do_dont_pattern, data_in):
    """
    :param do_dont_pattern: A regex pattern describing do or don't operation
    :param data_in: input data string with patterns in it
    :return: a list of start indices where the given do or don't pattern occurs.
    """
    output = []
    for pattern in re.finditer(do_dont_pattern, data_in):
        output.append(pattern.start())
    return output

# Regex expressions
mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
dont_mul_pattern = re.compile(r"don't\(\)")
do_mul_pattern = re.compile(r"do\(\)")

# Import data as a big string
data = aoc_utils.import_data_as_string(example=False)
print(data)

# Get the indices where do and don't operations occur.
do_inxs = get_start_stop_inx(do_mul_pattern, data)
dont_inxs = get_start_stop_inx(dont_mul_pattern, data)
do_inxs = [0] + do_inxs
print("DO Indices:\n", do_inxs, "\nDONT Indices:\n", dont_inxs)

# Create a "mask" so that we can filter out the parts of the string that contain invalid mul operations
data_mask = []
add_char = True
for inx, d in enumerate(data):
    if inx in do_inxs:
        add_char = True
    elif inx in dont_inxs:
        add_char = False

    if add_char:
        data_mask.append(True)
    else:
        data_mask.append(False)
print("DATA MASK:\n", data_mask)

# Create a new string with only the unmasked data
masked_data = []
for m, d in zip(data_mask, data):
    if m:
        masked_data.append(d)
masked_data = ''.join(map(str, masked_data))
print("MASKED DATA:\n", masked_data)

# Total up the multiplications as before in part 1
total = 0
for pattern in re.finditer(mul_pattern, masked_data):
    mult_val = int(pattern.group(1))*int(pattern.group(2))
    total += mult_val

print(total)
