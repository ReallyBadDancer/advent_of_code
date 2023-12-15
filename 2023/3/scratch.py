import re
from pprint import pprint

test = True

ifilename = "example_input" if test else "puzzle_input"

with open(ifilename) as ifile:
    test_input = ifile.read().splitlines()

pprint(test_input)
