from pprint import pp
from itertools import cycle
import re

input_type = 'p'
input_types = {'v':'test_vector', 'e': 'example_input', 'p': 'puzzle_input'}
ifilename = input_types[input_type]

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.readlines()
data = [i.strip() for i in data]

print("\nExtract directions:")
directions = data[0]
# print(directions)
directions = cycle(directions)  # Create an infinite cycle of directions.

print("\nParse network nodes into lists:")
network = []
for n in data[2:]:
    node = re.finditer(r"[A-Z]{3}", n)
    temp_node = []
    for i in node:
        temp_node.append(i.group())
    network.append(temp_node)
# print(network)

curr_loc = 'AAA'
print(f"First Location: {curr_loc}")
nodes = {n[0]: {'L': n[1], 'R': n[2]} for n in network}
# pp(nodes)

hops = 0
for d in directions:
    next_loc = nodes[curr_loc][d]
    print(f"Location: {curr_loc}:{nodes[curr_loc]}. Going {d} to {next_loc}. Total Hops: {hops}")
    curr_loc = next_loc
    hops += 1
    if curr_loc == 'ZZZ':
        print(f"Found {curr_loc}. Total hops: {hops}")
        break

print("Part 1 Answer: ", hops)
