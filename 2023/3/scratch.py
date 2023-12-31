import re
from pprint import pprint

test = True

ifilename = "example_input" if test else "puzzle_input"

with open(ifilename) as ifile:
    test_input = ifile.read().splitlines()

pprint(test_input)

for line in test_input:
    print(line)
    for match in re.finditer(r"\d+", line):
        print(match.group(0), match.start(0), match.end(0))
        print(line[match.start(0):match.end(0)])

