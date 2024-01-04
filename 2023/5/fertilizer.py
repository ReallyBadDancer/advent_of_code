import string
from pprint import pprint
from collections import deque
import re


def get_map_values(almanac_data: list, map_type: dict) -> dict:
    """
    Parses a list of almanac data to extract source/destination ranges and updates the provided dictionary.

    This function iterates over the provided almanac data until it encounters an empty line, which signifies
    the end of the current map type. For each line, it finds all occurrences of integers and appends them as
    a list to `curr_ranges`. Finally, it adds `curr_ranges` to the `map_type` dictionary under the key 'Ranges'.

    Args:
        almanac_data (list): A list of strings representing the almanac data.
        map_type (dict): The dictionary to be updated with the source/destination ranges.

    Returns:
        dict: The updated `map_type` dictionary containing the source, destination, and applicable ranges
        to be mapped. The ranges are represented as a list of lists of integers.
    """

    curr_ranges: list[dict]
    curr_ranges = []
    for line in almanac_data:
        if line == '':
            break
        else:
            sub_range = []
            for num in re.finditer('\d+', line):
                sub_range.append(int(num.group()))
            sub_range_dict = {'source start': sub_range[1], 'dest start': sub_range[0], 'length': sub_range[2]}
            curr_ranges.append(sub_range_dict)
    map_type['Ranges'] = curr_ranges
    return map_type


def get_next_no_from_ranges(curr_no:int, curr_map:dict) -> int:
    # Check if the curr_no is in any of the ranges
    ranges = []
    for item in curr_map['Ranges']:
        ranges.append(list(range(item['source start'],
                                 item['source start']+item['length'])))
    # If it isn't in any of the ranges, then return curr_no (not mapped)
    # If the curr_no is in a range, then return (dest_start - source_start) + curr_no
    print(ranges)
    return 0


test = True
part_one = True
ifilename = "example_input" if test else "puzzle_input"

with open(ifilename) as ifile:
    data = ifile.read().splitlines()

# Get the list of seeds from the first line of the data input
seeds = re.finditer('\d+', data[0])
seed_list = []
for seed in seeds:
    seed_list.append(int(seed.group()))
print('Seed list: \n----\n', seed_list)

# Generate a deque list of maps from the data set in the form of a list of Source/Destination dicts
map_types = [
    ['seed', 'soil'],
    ['soil', 'fertilizer'],
    ['fertilizer', 'water'],
    ['water', 'light'],
    ['light', 'temperature'],
    ['temperature', 'humidity'],
    ['humidity', 'location'],
]
map_types = [{'Source': item[0], 'Destination': item[1]} for item in map_types]
map_types = deque(map_types)
print("Map Types:\n----")
pprint(map_types)

# Add a list of source/dest map ranges to each map type in the almanac (excluding the seeds themselves) to get a dict
# with {Source, Destination, Ranges}
maps = []
data = data[2:]
for inx, line in enumerate(data):
    if line and line[0] in string.ascii_lowercase:  # Indicates a map start
        map_type = map_types.popleft()
        maps.append(get_map_values(data[inx+1:], map_type))
print('\nParsed source/destination maps:\n----')
pprint(maps)

print('\nGetting location of each seed:')
destinations = [
    'soil',
    'fertilizer',
    'water',
    'light',
    'temperature',
    'humidity',
    'location'
]
locations = []
for seed in seed_list:
    location = 0
    print(f'Calculation for seed {seed}...')
    curr_no = seed
    for destination in destinations:  # Walk through all of the different destinations from top to bottom
        for map_dict in maps:  # Flip through the maps to find current destination.
            if map_dict['Destination'] == destination:
                curr_no = get_next_no_from_ranges(curr_no, map_dict)
                print(curr_no)





