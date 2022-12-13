import numpy as np


class Tree:
    def __init__(self, height):
        self.visible = 0
        self.height = height
        self.n_score = 0
        self.s_score = 0
        self.e_score = 0
        self.w_score = 0
        self.scenic_score = 1

    def calculate_scenic_score(self):
        self.scenic_score = self.n_score * self.s_score * self.e_score * self.w_score

    def __repr__(self):
        # return f"<h,n,s,e,w,score: {self.height}, {self.n_score}, {self.s_score}, {self.e_score}, {self.w_score}, {self.scenic_score}>"
        return f"<{self.scenic_score}>"

with open("example_input.txt") as infile:
# with open("puzzle_input.txt") as infile:
    data = infile.read().split('\n')

tree_rows = []
for y_inx, line in enumerate(data):
    row = []
    for x_inx, item in enumerate(line):
        row.append(Tree(int(item)))
    tree_rows.append(row)

tree_array = np.array(tree_rows)
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


visible_trees = 0
for row in tree_rows:
    for tree in row:
        visible_trees += tree.visible

print(f"Part 1 answer: {visible_trees}")

# Assign 0 for all trees on edges.
for tree in tree_array[0]:
    tree.n_score=0
for tree in tree_array[grid_size-1]:
    tree.s_score=0
for tree in tree_array[:,0]:
    tree.w_score=0
for tree in tree_array[:, grid_size-1]:
    tree.e_score=0

# Calculate n_scores and s_scores for North and South-looking scenery.
for x in range(grid_size):
    for y in range(grid_size):
        curr_tree = tree_array[y, x]
        y_temp = y
        while y_temp != 0 and tree_array[y_temp-1][x].height < tree_array[y, x].height:
            tree_array[y, x].n_score += 1
            y_temp -= 1
            if y_temp == 0:
                tree_array[y, x].n_score += 1
        y_temp = y
        while y_temp < grid_size-1 and tree_array[y_temp+1][x].height < tree_array[y, x].height:
            tree_array[y, x].s_score += 1
            y_temp += 1
            if y_temp == grid_size-1:
                tree_array[y, x].n_score += 1

for y in range(grid_size):
    for x in range(grid_size):
        curr_tree = tree_array[y, x]
        x_temp = x
        while x_temp != 0 and tree_array[y][x_temp-1].height < tree_array[y, x].height:
            tree_array[y, x].w_score += 1
            x_temp -= 1
            if x_temp == 0:
                tree_array[y, x].w_score += 1
        x_temp = x
        while x_temp < grid_size-1 and tree_array[y][x_temp+1].height < tree_array[y, x].height:
            tree_array[y, x].e_score += 1
            x_temp += 1
            if x_temp == grid_size-1:
                tree_array[y, x].e_score += 1


for y in range(grid_size):
    for x in range(grid_size):
        curr_tree = tree_array[y,x]
        tree_array[y, x].calculate_scenic_score()

print(tree_array)




