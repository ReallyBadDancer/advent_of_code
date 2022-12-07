import sys
from parse import parse
from anytree import Node, RenderTree, PreOrderIter

dir_sizes = []

# This funciton is broken AF right now.
def calculate_directory_size(node: Node):
    # print(f"Calculating size of {node}")
    total_size = 0
    for inx, child in enumerate(PreOrderIter(node)):
        if inx == 0:
            continue
        elif child.type == 'file':
            total_size += child.size
        else:
            calculate_directory_size(child)
    if node.type == 'dir':
        node.size = total_size
        dir_sizes.append(node.size)
        if node.size < 100000:
            print(f"{node.name} ({node.type}) final size: {node.size}")
    return total_size


def select_child_node(name_str: str, current_node: Node):
    for node in current_node.children:
        if node.name == name_str:
            return node
    return None


# with open("example_input.txt", mode='r') as infile:
with open("puzzle_input.txt", mode='r') as infile:
    data = infile.read().split('\n')

root = Node(name='root', type='dir', size=0)
current_dir = root

node_list = []
for line in data[1:]:
    if "$ ls" in line:
        continue
    elif "$ cd .." in line:
        current_dir = current_dir.parent
    elif "$ cd" in line:
        new_dirname = parse("$ cd {}", line)[0]
        if select_child_node(new_dirname, current_dir):
            current_dir = select_child_node(new_dirname, current_dir)
        else:
            print("Warning: New dir Created with $ cd")
            new_dir = Node(new_dirname, type='dir', size=0, parent=current_dir)
            node_list.append(new_dir)
            current_dir = new_dir
    elif 'dir' in line:
        new_dirname = parse("dir {}", line)[0]
        if select_child_node(new_dirname, current_dir):
            continue
        else:
            new_dir = Node(new_dirname, type='dir', size=0, parent=current_dir)
            node_list.append(new_dir)
    elif line[0] in "0123456789":
        file_data = parse("{} {}", line)
        if select_child_node(file_data[1], current_dir):
            continue
        else:
            new_file = Node(file_data[1], type='file', size=int(file_data[0]), parent=current_dir)
            node_list.append(new_file)

root.size = calculate_directory_size(root)
print(f"Total file system size {root.size}")

# Part 1
answer = 0
for i in set(dir_sizes):
    answer += i
print(f"answer part 1: {answer}")

# Part 2
required_space = 30000000
drive_size = 70000000
available_space = drive_size - root.size
min_data_to_delete = required_space - available_space
deletion_candidates = []
for i in set(dir_sizes):
    if i > min_data_to_delete:
        deletion_candidates.append(i)

print(f"answer part 2: {min(deletion_candidates)}")

