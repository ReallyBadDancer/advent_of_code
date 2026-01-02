from math import dist
from pprint import pprint

EXAMPLE = True

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = [list(map(int, line.split(','))) for line in f]

    # pprint(data)
    
    distance_matrix = []
    for i, row in enumerate(data):
        distances = []
        for col in data[i+1:]:
            distances.append(dist(row,col))
        distance_matrix.append(distances)
    
    # print("Distances:")
    # pprint(distance_matrix)
    
    # Find the ten shortest distances (connections) and store them as a list of coordinates. 
    # Group together the pairs into circuits, discarding duplicates using sets.
    # Drop all circuits except the top three and multiply the sizes together.
    
    distance_pairs = {}
    for row_i, row in enumerate(distance_matrix):        
        # print(f"Starting row {row_i}\nDistance Pairs: {distance_pairs}\n")
        for dist_i, dist in enumerate(row):
            # This accounts for the triangle shape of the matrix, plus skipping the first element, which is always zero.
            distance_pairs[dist] = [row_i, dist_i+row_i+1]   
       
    box_pairs = []
    for dist in sorted(distance_pairs):
        if len(box_pairs) == 10:
            break
        box_pairs.append(distance_pairs[dist])
    
    # print("Box pairs:")
    box_pairs = sorted(box_pairs)
    # pprint(box_pairs)
    
    circuits = []    
    circuits.append(set(box_pairs.pop(0)))
    while box_pairs:
        curr_circuit = set(box_pairs.pop(0))
        for inx, c in enumerate(circuits):
            if curr_circuit & c:
                c = c.union(curr_circuit)
                circuits[inx] = c
                break
        else:
            circuits.append(curr_circuit)
    
    print("Circuits:")
    pprint(circuits)
    
    
        
        
            
                
            
            
            