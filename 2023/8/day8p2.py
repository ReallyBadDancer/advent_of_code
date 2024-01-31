from pprint import pp
from itertools import cycle
import re
import math
import time

input_type = 'p'
input_types = {'v': 'test_vector', 'e': 'example_input', 'p': 'puzzle_input'}
ifilename = input_types[input_type]

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.readlines()
data = [i.strip() for i in data]

print("\nExtract directions:")
directions = data[0]
print(directions)
directions = cycle(directions)  # Create an infinite cycle of directions.

print("\nParse network nodes into lists:")
network = []
start_nodes = []
for n in data[2:]:
    node = re.finditer(r"[A-Z0-9]{3}", n)
    temp_node = []
    for i in node:
        temp_node.append(i.group())
    network.append(temp_node)
# pp(network)

print("\nGet a list of starting locations:")
starting_locs = []
for n in network:
    if n[0][-1] == 'A':
        starting_locs.append(n[0])
print(starting_locs)

print("\nCreate a dictionary of form {location: left, right}")
network = {n[0]: {'L': n[1], 'R': n[2]} for n in network}
# pp(network)

print("\nMake a ghost at each starting node:")


class Ghost:
    def __init__(self, loc, network):
        self.loc = loc
        self.initial_loc = loc
        self.network = network
        self.multiple = 0

    def hop(self, direction: str, hop_no: int):
        new_loc = self.network[self.loc][direction]
        # print(f"Ghost at {self.loc} going {direction} to {new_loc}")
        self.loc = new_loc
        if self.loc[-1] == 'Z':
            print(f"Ghost {self.initial_loc} found ending at {self.loc} on hop {hop_no}")
            if not self.multiple:
                self.multiple = hop_no
            return True

    def __repr__(self):
        return f"Ghost {self.initial_loc} at {self.loc} with multiple {self.multiple}"


ghosts = [Ghost(i, network) for i in starting_locs]
pp(ghosts)

print("Determine how many hops it takes for each ghost to get to its first 'Z' ending: ")
hops = 1
ghosts_with_multiple = []
for d in directions:
    if all([g.multiple for g in ghosts]):  # All ghosts have a multiple
        break
    for g in ghosts:
        if g.hop(d, hops):
            ghosts_with_multiple.append(g)
            print(hops, ghosts)
    hops += 1

multiple_list = []
for g in ghosts_with_multiple:
    multiple_list.append(g.multiple)
    print(g)

print(f"List of multiples: {multiple_list}. Get least-common multiple:")

wrong_answers = [776131132920, 6804426182583304574940480]
answer2 = math.lcm(*multiple_list)
print("Part 2 Answer: ", answer2)
if answer2 in wrong_answers:
    print("This answer is wrong.")
if answer2 == 14299763833181:
    print("This answer is probably correct.")
