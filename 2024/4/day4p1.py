from aoc_utils import import_data_as_lines
import re

data = import_data_as_lines(example=True)
print(data)

total = 0
for row in data:
    for item in re.finditer(r"XMAS", row):
        print(f"Found forward in {row}")
        total += 1
    for item in re.finditer(r"SAMX", row):
        print(f"Found reversed in {row}")
        total += 1

transposed_data = [[row[i] for row in data] for i in range(len(data[0]))]
print("Transposed Data:\n", transposed_data)


print(total)
