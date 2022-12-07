from parse import parse

class ElfFile:
    def __init__(self, name, type, size, children, parent):




with open("example_input.txt", mode='r') as infile:
    data = infile.read().split('\n')



curr_dir = {
    'name': 'root',
    'type': 'dir',
    'size': 0,
    'children': {},
    'parent': None
}

for line in data[1:]:
    if "$ ls" in line:
        continue
    elif "cd .." in line:
        curr_dir = curr_dir['parent']
    elif "$ cd" in line:
        new_dirname = parse("cd {}", line)
        if new_dirname in curr_dir.children:
            curr_dir = curr_dir[new_dirname]
        else:
            pass
