import sys
from parse import parse
from anytree import Node, RenderTree, PreOrderIter


class Tree:
    def __init__(self, height):
        self.visible = 0
        self.height = height

    def __repr__(self):
        return f"{self.visible}"



# with open("puzzle_input.txt", mode='r') as infile:
with open("example_input.txt") as infile:
    data = infile.read().split('\n')

tree_rows = []
for y_inx, line in enumerate(data):
    row = []
    for x_inx, item in enumerate(line):
        row.append(Tree(int(item)))
    tree_rows.append(row)

grid_size = len(tree_rows[0])

# Top and bottom row
for y in [0, grid_size-1]:
    for x in range(grid_size):
        tree_rows[y][x].visible = 1

# First and last column
for x in [0, grid_size-1]:
    for y in range(grid_size):
        tree_rows[y][x].visible = 1

# Row by row, forward
for y in range(0, grid_size):
    h_max = 0
    for x in range(0, grid_size):
        if tree_rows[y][x].height > h_max:
            h_max = tree_rows[y][x].height
            tree_rows[y][x].visible = 1

# Row by row, backward
for y in range(0, grid_size):
    h_max = 0
    for x in range(grid_size-1, 0, -1):
        if tree_rows[y][x].height > h_max:
            h_max = tree_rows[y][x].height
            tree_rows[y][x].visible = 1

# Column by column, forward
for x in range(0, grid_size):
    h_max = 0
    for y in range(0, grid_size):
        if tree_rows[y][x].height > h_max:
            h_max = tree_rows[y][x].height
            tree_rows[y][x].visible = 1

# Column by column, backward
for x in range(0, grid_size):
    h_max = 0
    for y in range(grid_size-1, 0, -1):
        if tree_rows[y][x].height > h_max:
            h_max = tree_rows[y][x].height
            tree_rows[y][x].visible = 1

for row in tree_rows:
    print(row)

visible_trees = 0
for row in tree_rows:
    for tree in row:
        visible_trees += tree.visible

print(visible_trees
      )