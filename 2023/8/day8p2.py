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
# print(data)

print("\nExtract directions:")
directions = data[0]
print(directions)
directions = cycle(directions)  # Create an infinite cycle of directions.

print("\nParse network nodes into lists, also get a list of starting nodes:")
network = []
start_nodes = []
for n in data[2:]:
    node = re.finditer(r"[A-Z0-9]{3}", n)
    temp_node = []
    for i in node:
        temp_node.append(i.group())
    network.append(temp_node)
pp(network)

print("\nGet a list of starting locations:")
starting_locs = []
for n in network:
    if n[0][-1] == 'A':
        starting_locs.append(n[0])
print(starting_locs)

print("\nCreate a dictionary of form {location: left, right}")
network = {n[0]: {'L': n[1], 'R': n[2]} for n in network}
pp(network)

print("\nMake a ghost at each starting node:")


class Ghost:
    def __init__(self, loc, network):
        self.loc = loc
        self.network = network

    def hop(self, direction: str):
        new_loc = self.network[self.loc][direction]
        # print(f"Ghost at {self.loc} going {direction} to {new_loc}")
        self.loc = new_loc
        if self.loc[-1] == 'Z':
            return True

    def __repr__(self):
        return f"Ghost at {self.loc}"


ghosts = [Ghost(l, network) for l in starting_locs]
pp(ghosts)

hops = 1
for d in directions:
    if hops % 1e6 == 0:
        print(f"Hop {hops}. Going {d}")
    if all([g.hop(d) for g in ghosts]):
        print("Part 2 Answer: ", hops)
        exit(0)
    else:
        hops += 1
    #
    # next_loc = network[curr_loc][d]
    # print(f"Location: {curr_loc}:{network[curr_loc]}. Going {d} to {next_loc}. Total Hops: {hops}")
    # curr_loc = next_loc
    # hops += 1
    # if curr_loc == 'ZZZ':
    #     print(f"Found {curr_loc}. Total hops: {hops}")
    #     break


