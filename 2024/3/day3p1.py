import aoc_utils
import re

mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
dont_mul_pattern = re.compile(r"don't\(\)")
do_mul_pattern = re.compile(r"do\(\)")

data = aoc_utils.import_data_as_string(example=False)
print(data)

total = 0
for pattern in re.finditer(mul_pattern, data):
    mult_val = int(pattern.group(1))*int(pattern.group(2))
    total += mult_val

print(total)
