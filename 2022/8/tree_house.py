import sys
from parse import parse
from anytree import Node, RenderTree, PreOrderIter


class Tree:
    def __init__(self, height):
        self.visible = 0
        self.height = height

    def __repr__(self):
        return f"<h: {self.height}, vis: {self.visible}>"


# with open("puzzle_input.txt", mode='r') as infile:
with open("example_input.txt") as infile:
    data = infile.read().split('\n')

tree_rows = []
for y_inx, line in enumerate(data):
    row = []
    for x_inx, item in enumerate(line):
        row.append(Tree(int(item)))
    tree_rows.append(row)

# print(tree_rows)


# Assign all edges visible
for y, tree_row in enumerate(tree_rows):
    for x, tree in enumerate(tree_row):
        if y == 0 or y == len(tree_rows)-1:
            tree.visible = 1
        elif x == 0 or x == len(tree_row)-1:
            tree.visible = 1

# Walk left to right
for y, tree_row in enumerate(tree_rows):
    h_max = 0
    for x, tree in enumerate(tree_row):
        if tree.height > h_max:
            h_max = tree.height
            tree.visible = 1

# Walk right to left
for y, tree_row in enumerate(tree_rows):
    h_max = 0
    for x, tree in reversed(list(enumerate(tree_row))):
        if tree.height > h_max:
            h_max = tree.height
            tree.visible = 1

# Walk top to bottom
for y, tree_row in enumerate(tree_rows):
    h_max = 0












for row in tree_rows:
    print(row)

