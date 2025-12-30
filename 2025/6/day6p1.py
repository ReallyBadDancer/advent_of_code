from math import prod

EXAMPLE = True

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.read().splitlines()
        *rows, operations = data
        data = [r.split() for r in rows]
        data = [list(map(int, d)) for d in data]
        operations = operations.split()
        print(data, operations)

    op_funcs = []
    for op in operations:
        if op == '*':
            op_funcs.append(prod)
        else:
            op_funcs.append(sum)

    grand_total = 0
    for i in range(len(data[0])):
        temp_vals = [val[i] for val in data]
        grand_total += op_funcs[i](temp_vals)

    print(grand_total)
