# Create two lists of numbers
# Sort each list of numbers from smallest to largest
# Get a third list of differences

part_1 = False
use_example = False

example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("puzzle_input") as ifile:
    puzzle_input = ifile.read()

data = example_input if use_example else puzzle_input

loc_lists = [[], []]
for line in data.splitlines():
    for l, loc in zip(loc_lists, line.split("   ")):
        l.append(int(loc))
print(loc_lists)


if part_1:
    for l in loc_lists:
        l.sort()
    print(loc_lists)

    tuple_list = [(i, j) for i, j in zip(*loc_lists)]
    print(tuple_list)

    diff_list = [abs(j-i) for i,j in tuple_list]
    print(diff_list)

    print(sum(diff_list))
else:
    sim_sum = 0
    for l1 in loc_lists[0]:
        for l2 in loc_lists[1]:
            if l1 == l2:
                sim_sum += l1

print(sim_sum)
