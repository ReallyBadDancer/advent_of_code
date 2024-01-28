from pprint import pp

test = True
ifilename = "example_input" if test else "puzzle_input"

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.read()
pp(data)
