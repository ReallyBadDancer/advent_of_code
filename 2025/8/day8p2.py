from math import dist
from pprint import pprint
from collections import Counter

EXAMPLE = False
LIMIT = 10 if EXAMPLE else 1000

if __name__ == "__main__":

    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = [list(map(int, line.split(','))) for line in f]
    print("Data: ")
    # pprint(data)

    # Get a list of all distances and pairs.
    pairs = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            d = dist(data[i], data[j])
            pairs.append((d, i, j))
    pairs.sort()
    print("Pairs: ")
    # pprint(pairs)

    parents = [i for i in range(len(data))]


    def find(x: int) -> int:
        while parents[x] != x:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return parents[x]


    def union(x: int, y: int) -> None:
        px, py = find(x), find(y)
        if px == py:
            return
        elif px != py:
            parents[py] = px
        else:
            print("Error in union")
            exit(1)


    def one_big_circuit():
        circuits = [find(i) for i in range(len(data))]  # This produces a list of roots.
        # print("Circuits: ")
        # pprint(circuits)
        return all([i == circuits[0] for i in circuits])
    
    # Merge down each pair in the list to generate a "tree" of circuits, each leading to a root.    
    for idx, (_, x, y) in enumerate(pairs):        
        if not one_big_circuit():
            print("Last X coordinates: ", data[x][0], data[y][0])
            candidate_answer = data[x][0] * data[y][0]
            union(x, y)
        else:
            print("Last X coordinates: ", data[x][0], data[y][0])
            candidate_answer = data[x][0] * data[y][0]
            break

    print("Parents: ")
    print(parents)

    circuits = [find(i) for i in range(len(data))]  # This produces a list of roots.
    print("Circuits: ")
    # print(circuits)

    # groups = Counter(circuits)
    # print("Groups: ")
    # print(groups)
    print("Answer: ")
    print(candidate_answer)
    # sizes = sorted(groups.values(), reverse=True)
    # # print("Sizes: ", sizes)
    # 
    # print("Answer: ", sizes[0] * sizes[1] * sizes[2])
