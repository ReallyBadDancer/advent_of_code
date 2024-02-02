from pprint import pp
from math import ceil

input_type = 'p'
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
# pp(data)


class Critter:
    valid_directions = {
        'l': '-LF',
        'r': '-J7',
        'u': '|7F',
        'd': '|JL',
    }
    pipe_openings = {
        '|': ('u', 'd'),
        '-': ('l', 'r'),
        'L': ('u', 'r'),
        'J': ('u', 'l'),
        '7': ('l', 'd'),
        'F': ('r', 'd'),
        'S': ('l', 'r', 'u', 'd'),
    }

    def __init__(self, pipe_map):
        self.pipe_map = pipe_map
        for row_inx, row in enumerate(self.pipe_map):
            for col_inx, col in enumerate(row):
                if col == 'S':
                    self.pos = (row_inx, col_inx)
                    print("Initialized critter at: ", self.pos)
        self.position_history = [self.pos]

    def start(self):
        pass

    def move(self):
        moves = {
            'l': (self.pos[0], self.pos[1]-1),
            'r': (self.pos[0], self.pos[1]+1),
            'u': (self.pos[0]-1, self.pos[1]),
            'd': (self.pos[0]+1, self.pos[1]),
        }
        curr_pipe_shape = self.pipe_map[self.pos[0]][self.pos[1]]
        for direction, coord in moves.items():
            if (self.pipe_map[coord[0]][coord[1]] in self.valid_directions[direction] and
                    coord not in self.position_history and
                    direction in self.pipe_openings[curr_pipe_shape]):
                self.pos = coord
                self.position_history.append(coord)
                print("Critter moved to ", self.pos)
                return True
        else:
            return False


c = Critter(data)
while c.move():
    print("Moving...")

print(f"The answer to part 1 is: {ceil(len(c.position_history)/2)}")
