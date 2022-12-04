
with open('puzzle_input.txt', mode='r') as ifile:
# with open('example_input.txt', mode='r') as ifile:
    data = ifile.read().split('\n')
    print(data)

# Break the data into pairs of sector ranges, then
# Convert dash-separated ranges into individual lists, then
# Convert all string numbers into integers.
# Final format is a list of all pairs, where each pair is a pair of [begin, end] sector ranges.
sector_pairs = []
for item in data:
    pair = item.split(',')
    # print(pair)
    range_pair = []
    for sector_range in pair:
        sector_range = sector_range.split('-')
        # print(sector_range)
        range_pair.append([int(i) for i in sector_range])
    sector_pairs.append(range_pair)
print(sector_pairs)

# Take each sector pair and "expand" the range to contain all numbers that are members of the range by replacing each
# element of each pair and individually reassigning it.
expanded_sector_pairs = []
for pair in sector_pairs:
    for inx, sector_range in enumerate(pair):
        expanded_sector = []
        for loc in range(sector_range[0], sector_range[1]+1):
            expanded_sector.append(loc)
        pair[inx] = expanded_sector
        # print(expanded_sector)
    expanded_sector_pairs.append(pair)
# print(f"Expanded pairs: {expanded_sector_pairs}")

# This is a copypasta from https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
# I think the all() statement works by walking through all items in the pair[n] after the "for" statement and
# comparing it to the elements in pair[m] one by one.
fully_redundant_pair_count = 0
for pair in expanded_sector_pairs:
    if all(loc in pair[0] for loc in pair[1]) or all(loc in pair[1] for loc in pair[0]):
        # print(pair)
        fully_redundant_pair_count += 1

print(f"Total completely redundant pairs: {fully_redundant_pair_count}")

# ------------
# Begin Part 2
# ------------

# This part is easy today since it's just an "or" of the lists instead of an "and." Therefore the only difference is
# I use the any() function instead of the all() function. Also no need to check twice this time.
partially_redundant_pair_count = 0
for pair in expanded_sector_pairs:
    if any(loc in pair[0] for loc in pair[1]):
        # print(pair)
        partially_redundant_pair_count += 1

print(f"Total partially redundant pairs: {partially_redundant_pair_count}")