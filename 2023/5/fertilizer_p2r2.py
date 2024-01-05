# I gave up on this one and just copied the solution by hyper-neutrino. I couldn't write my own version without
# basically 100% copying it given how many hours I spent studying it. I just annotated it as an exercise and added
# Some prints to better understand how it works.
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py

inputs, *blocks = open('puzzle_input').read().split("\n\n")  # Break into parts using double newline.
print("Inputs:", inputs)
inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []
for i in range(0, len(inputs), 2):  # Create a seed range of tuples of form (start range inx, end range inx)
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))
print(seeds)

for block in blocks:
    print("\nProcessing block:", block.splitlines()[0])
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))  # Process blocks here.
    print("Ranges processed: \n", ranges)
    new = []  # New is the next set of ranges to generate as input to the next block.
    while len(seeds) > 0:
        print("Current state of seeds: ", seeds)
        print("Current state of next map: ", new)
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:  # This is the case where overlap exists (overlap start index has to be less than overlap end)
                new.append((os - b + a, oe - b + a))  # Add to the next mapping if there is overlap
                if os > s:  # Check for a range of seeds that is before the overlap and add it to seeds in curr block.
                    seeds.append((s, os))  # Could be that these seeds are mapped elsewhere in the current block.
                if e > oe:  # Check for a range of seeds that is after the overlap and add it to seeds in curr block.
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))  # If we didn't encounter a break (there was no overlap) then just carry to next block.)
    seeds = new

print(min(seeds)[0])
