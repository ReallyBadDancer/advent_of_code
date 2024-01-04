# Solution heavily borrowed from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
# My solution was becoming convoluted, so I wanted to use it as a learning exercise instead.

from pprint import pprint
import re

test = False
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
print("\nAlmanac Maps")
pprint(almanac_maps)

class AlmanacMap:
    def __init__(self, almanac_map):
        self.almanac_map = almanac_map.split("\n")[1:] # Drop the title from data.
        self.almanac_name = almanac_map.split("\n")[0] # Grab title for funsies.
        print("Creating new map: ", self.almanac_name, self.almanac_map)
        self.almanac_data = []
        for m in self.almanac_map:  # I don't like nested list comps.
            n = [int(i.group()) for i in re.finditer("\d+", m)]
            self.almanac_data.append(n)
        print("Integer maps:")
        print(self.almanac_data)
    def find_location(self, x):
        print(f"Finding location for {self.almanac_name} on seed {x}")
        for [dest, source, length] in self.almanac_data:
            if (source <= x < source + length):
                print("Got ", x + dest - source)
                return x + dest - source
        print("Got no map, so ", x)
        return x


almanacs = []
for almanac in almanac_maps:
    almanacs.append(AlmanacMap(almanac))

# Part 1 solution
P1 = []
for seed in seeds:
    for almanac in almanacs:
        seed = almanac.find_location(seed)
    P1.append(seed)
print("\nAnswer for part 1:")
print(min(P1))



