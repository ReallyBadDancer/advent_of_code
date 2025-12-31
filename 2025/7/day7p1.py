from pprint import pprint

EXAMPLE = False

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.read().splitlines()
    
    data = [list(i) for i in data]
    print("Data: ")
    pprint(data)
    
    splits = 0
    for i in range(len(data)):        
        # print(data[i])
        if i == len(data) - 1:
            break
        for inx, c in enumerate(data[i]):
            if inx == 0:
                continue
            if data[i - 1][inx] in ('S', '|'):
                if c == '^':  # Handle splitters
                    splits += 1
                    data[i][inx-1] = '|'
                    data[i][inx+1] = '|'
                else:
                    data[i][inx] = '|'
    
    print("Modified Data: ")
    pprint(data)
    print("Split Counts: ", splits)