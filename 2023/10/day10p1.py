from pprint import pp

input_type = 'e'
input_types = {'v': 'test_vector', 'e': 'example_input', 'p': 'puzzle_input'}
ifilename = input_types[input_type]

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.readlines()
data = [list(i.strip()) for i in data]

print("\nAdd padding")
horizontal_border = ['.' for i in range(len(data[0]))]
data = [horizontal_border] + data + [horizontal_border]
data = [['.'] + i + ['.'] for i in data]
pp(data)
