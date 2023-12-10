example_string = ['1 red', '2 green', '6 blue']

split_string = [c.split(' ') for c in example_string]
example_dict = {s[1]:int(s[0]) for s in split_string}

print(split_string)
print(example_dict)