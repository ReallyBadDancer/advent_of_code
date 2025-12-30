EXAMPLE = False

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.read().split("\n\n")
        ranges = data[0].split("\n")
        ranges_tuples = []
        for r in ranges:
            ranges_tuples.append(tuple(map(int,r.split('-'))))
        ids = data[1].split("\n")
        ids = list(map(int,ids))
        print(ids)
        print(ranges_tuples)

    fresh_counter = 0

    for i in ids:
        for r in ranges_tuples:
            # print("Is ID ", i, " in range ", r, "?")

            if i in range(r[0], r[1] + 1):
                fresh_counter += 1
                print(f"Ingredient {i} is fresh and in range {r[0]} to {r[1]}")
                break
        print(f"Ingredient {i} must be spoiled.")


    print(fresh_counter)


