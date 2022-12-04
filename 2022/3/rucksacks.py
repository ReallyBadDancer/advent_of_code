import string

# Begin part 1: Finding out which item is in both compartments of each rucksack.
# ------------------------------------------------------------------------------

# Get the data from file.
with open("puzzle_input.txt", mode='r') as ifile:
    data = ifile.read().split('\n')

# Gotta group up the elves for part 2
elf_groups = []
for i in range(0, len(data), 3):
    elf_groups.append([data[i], data[i+1], data[i+2]])


# Generate an ordered list of the alphabet to assign a numeric value to letters later by index.
priority_list = string.ascii_letters

# Generate 2 compartments by rucksack with equal number of items each.
rucksack_compartments = []
for line in data:
    half_items_index = int(len(line) / 2)
    first_compartment = line[:half_items_index]
    seconds_compartment = line[half_items_index:]
    # print(f"{first_compartment} -- {seconds_compartment}")
    rucksack_compartments.append([first_compartment, seconds_compartment])

# Find which item is in both compartments, add it to a list, then break to the next rucksack to avoid double counting.
prioritized_items = []
for sack in rucksack_compartments:
    for item in sack[0]:
        if item in sack[1]:
           prioritized_items.append(item)
           break


# Add up all priority items according to their priority from the priority_list.
items_sum = 0
for item in prioritized_items:
    item_priority = priority_list.index(item) + 1
    items_sum += item_priority

print(f"The final sum of prioritized items for part 1 is {items_sum}")

# Begin part 2: Finding which item is in all three rucksacks and assign to the "badges."
# -----------------------------------------------------------

badges = []
for group in elf_groups:
    for letter in priority_list:
        if letter in group[0] and letter in group[1] and letter in group[2]:
            badges.append(letter)
            break


# Sum all badge values together as in part 1.
items_sum = 0
for item in badges:
    item_priority = priority_list.index(item) + 1
    items_sum += item_priority

print(f"The final sum of all badge item values for part 2 is {items_sum}")
