from collections import deque


def compare_current_symbols(symbol_list: deque) -> bool:
    temp_list = symbol_list.copy()  # Create a shallow copy to avoid manipulating outer scope list.
    for sym in temp_list.copy():  # Create ANOTHER shallow copy to avoid mutating a list we are iterating over.
        temp_list.popleft()
        if sym in temp_list:
            return False
    return True


# with open("example_input.txt", mode='r') as infile:
with open("puzzle_input.txt", mode='r') as infile:
    data = infile.read()
    print(data)

part_one = False
marker = 4 if part_one else 14

data_string = deque(data[:marker])
print(data_string)
if compare_current_symbols(data_string):
    print(data_string)

for symbol in data[marker:]:
    marker += 1
    data_string.popleft()
    data_string.append(symbol)
    if compare_current_symbols(data_string):
        print(data_string)
        print(marker)
        break
