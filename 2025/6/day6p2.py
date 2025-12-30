from math import prod
from pprint import pprint

EXAMPLE = True

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.read().splitlines()

    *rows, operations = data
    print(rows)
    print(operations)

    # Create a series of grids to work with.
    grid_start_indices = []
    for i, o in enumerate(operations):
        if o != " ":
            grid_start_indices.append(i)
    print(grid_start_indices)

    rows = [list(r) for r in rows]

    print("Rows: ")
    pprint(rows)

    grids = []
    for inx, i in enumerate(grid_start_indices):
        try:
            # max_index =
            grid = [r[grid_start_indices[inx]:grid_start_indices[inx+1]-1] for r in rows]
        except IndexError:
            grid = [r[grid_start_indices[inx]:] for r in rows]
        finally:
            grids.append(grid)
    print("Grids:")
    pprint(grids)

    def get_terms(number_grid: list[list[str]]) -> list[int]:
        nums = []
        for i in range(len(number_grid[0])-1, -1, -1):
            num = [g[i] for g in number_grid]
            nums.append(num)        
        nums = [int(''.join(i).strip()) for i in nums]        
        return nums

    terms = [get_terms(i) for i in grids]
    
    print("Terms: ")
    pprint(terms)

    operations = operations.split()
    
    print("Operations: ")
    print(operations)

    op_funcs = []
    for op in operations:
        if op == '*':
            op_funcs.append(prod)
        else:
            op_funcs.append(sum)

    grand_total = 0
    for t, o in zip (terms, op_funcs):
        grand_total += o(t)    
    
    print("Grand Total: ", grand_total)
    