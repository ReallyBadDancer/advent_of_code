# Solution heavily borrowed from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
# My solution was becoming convoluted, so I wanted to use it as a learning exercise instead.
# Also for part 2 watched https://youtu.be/NmxHw_bHhGM?si=fx-pz5ok7pNPX5Fv

from pprint import pprint
import re

test = True
part_one = True
ifilename = "example_input" if test else "puzzle_input"

with open(ifilename) as ifile:
    data = ifile.read()

# Get the seed numbers and then discard them from data
parts = data.split("\n\n")
print("\nParts")
pprint(parts)
seeds, *almanac_maps = parts  # This assigns the first element to seeds, and the rest to almanac maps, which is cool.
print("\nSeeds")
seeds = [int(i.group()) for i in re.finditer("\d+", seeds)]  # Finds all digits and puts them into a list of int
pprint(seeds)
print("\nSeed ranges (pairs): ")
pairs = list(zip(seeds[::2], seeds[1::2]))
print(pairs)

class AlmanacMap:
    def __init__(self, almanac_map):
        self.almanac_map = almanac_map.split("\n")[1:] # Drop the title from data.
        self.almanac_name = almanac_map.split("\n")[0] # Grab title for funsies.
        # print("Creating new map: ", self.almanac_name, self.almanac_map)
        self.almanac_data = []
        for m in self.almanac_map:  # I don't like nested list comps.
            n = [int(i.group()) for i in re.finditer("\d+", m)]
            self.almanac_data.append(tuple(n))
        print(f"Almanac Data for {self.almanac_name}:")
        print(self.almanac_data)
    def find_location(self, x):
        # print(f"Finding location for {self.almanac_name} on seed {x}")
        for [dest, source, length] in self.almanac_data:
            if (source <= x < source + length):
                # print("Got ", x + dest - source)
                return x + dest - source
        # print("Got no map, so ", x)
        return x

    def find_next_range(self, input_range:tuple):
        """Take in a range of input values and determines which of them overlap with the ranges in this set"""
        print(f"Finding overlap with current range {self.almanac_name}")
        input_s, input_l = input_range
        output = []
        leftover_input_segments = []
        for almanac_dest_s, almanac_src_s, almanac_l in self.almanac_data:  # Figure out if there is overlap on the edges of the input range
            overlap_start = max(input_s, almanac_src_s)
            overlap_end = min(input_s+input_l + almanac_src_s+almanac_l)
            if overlap_start < overlap_end:  # Checking for nonzero size of overlap
                output.append((overlap_start+almanac_dest_s-almanac_src_s,
                               overlap_end+almanac_dest_s-almanac_src_s))  # Add new mapped ranges to output.
            if input_s < overlap_start:  # Check for whether there is some unused section of the input range and if so, save it and put it back into the inputs for later checks.
                leftover_input_segments.append((input_s, overlap_start-input_s))
            if input_s + input_l > overlap_end:
                leftover_input_segments.append((overlap_end, input_s + input_l-overlap_end))
            break
        else:
            output.append(input_range)
        return output, leftover_input_segments




almanacs = []
for almanac in almanac_maps:
    almanacs.append(AlmanacMap(almanac))

# Part 1 solution
if part_one:
    P1 = []
    for seed in seeds:
        for almanac in almanacs:
            seed = almanac.find_location(seed)
        P1.append(seed)
    print("\nAnswer for part 1:")
    print(min(P1))

# Part 2 solution
P2 = []
while pairs:
    pair = pairs.pop()
    print(f"Finding pair overlap for {pair}")
    for almanac in almanacs:
        next_ranges, new_pairs = almanac.find_next_range(pair)




