import sys

class RopeSegment:
    def __init__(self, place, leader=None, head=False, tail=False):
        self.place = place
        self.leader = leader
        self.head = head
        self.tail = tail
        self.position_history = [[0, 0]]
        self.position = [0, 0]

    def __repr__(self):
        if self.leader:
            return f"<RopeSegment: (Place: {self.place}, Position: {self.position}, Leader: {self.leader.place}>"
        else:
            return f"<RopeSegment: (Place: {self.place}, Position: {self.position}, Leader: None>"

    def update_head_position(self, direction: str):
        if direction == 'R':
            self.position[0] += 1
        elif direction == 'L':
            self.position[0] -= 1
        elif direction == 'U':
            self.position[1] += 1
        elif direction == 'D':
            self.position[1] -= 1
        else:
            print("Error in updating head position")
        self.position_history.append(self.position)

    def update_position(self, direction: str):
        if self.head:
            self.update_head_position(direction)
        else:
            if abs(self.position[0] - self.leader.position[0]) <= 1 and abs(self.position[1] - self.leader.position[1]) <=1:
                return  # No position change if head and tail are close to each other
            elif any([abs(a - b) > 1 for a, b in zip(self.position, self.leader.position)]):  # Update one direction
                # print("Cardinal distance > 1 found.")
                for inx, pos in enumerate(self.leader.position):
                    if self.position[inx] != self.leader.position[inx]:
                        position_change = self.leader.position[inx] - self.position[inx]
                        position_change = position_change / abs(position_change)
                        self.position[inx] += position_change
            self.position_history.append(self.position.copy())


# Processing into an instruction list
# with open("example_input.txt") as infile:
with open("puzzle_input.txt") as infile:
    data = infile.read().split('\n')
instructions = [i.split(' ') for i in data]
instructions = [[a, int(b)] for [a, b] in instructions]


part_one = False
if part_one:
    rope_head = RopeSegment(0, head=True)
    rope_tail = RopeSegment(1, leader=rope_head, tail=True)
    rope = [rope_head, rope_tail]
else:
    rope = []
    for i in range(10):
        if rope:
            rope.append(RopeSegment(i, leader=rope[i-1]))
        else:
            rope.append(RopeSegment(i, head=True))

for step in instructions:
    for move in range(step[1]):
        for seg in rope:
            seg.update_position(step[0])
        # print(rope)

# print(rope_tail.position_history)
answer = set([tuple(i) for i in rope[-1].position_history])
print(len(answer))
