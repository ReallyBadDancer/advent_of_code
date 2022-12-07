import sys
from parse import parse
from anytree import Node, RenderTree


def select_child_dir(dir_str:str, current_node:Node)->Node:
    for node in current_node.children:
        if node.name == dir_str:
            return node


with open("example_input.txt", mode='r') as infile:
# with open("puzzle_input.txt", mode='r') as infile:
    data = infile.re ad().split('\n')

root = Node(name='root', type='dir', size=0)
current_dir = root

for line in data[1:]:
    if "$ ls" in line:
        continue
    elif "$ cd .." in line:
        current_dir = current_dir.parent
    elif "$ cd" in line:
        new_dirname = parse("$ cd {}", line)[0]
        if new_dirname in current_dir.children:
            current_dir = select_child_dir(new_dirname, current_dir)
        else:
            new_dir = Node(new_dirname, type='dir', size=0, parent=current_dir)
            current_dir = new_dir

print(RenderTree(root))

