from pprint import pprint

EXAMPLE = False

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = [list(map(int, line.split(','))) for line in f]
    print("Data: ")
    pprint(data)
    
    areas = []
    for i in range(len(data)):
        for j in range(i,len(data)):
            area = abs(data[i][0] - data[j][0]+1) * abs(data[i][1] - data[j][1]+1)
            areas.append(area)    
    print(max(areas))