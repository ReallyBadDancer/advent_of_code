EXAMPLE = False

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        data = f.read().split("\n\n")
        ranges = data[0].split("\n")
        range_lists = []
        for r in ranges:
            range_lists.append(list(map(int,r.split('-'))))
        ids = data[1].split("\n")
        ids = list(map(int,ids))
        # print(ids)
        # print(range_lists)

    # Had to learn how to merge ranges the easy way: By sorting them first.

    range_lists.sort(key=lambda x: x[0])

    merged = []
    for start, end in range_lists:
        # If merged is empty OR no overlap, append
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        # There is overlap at the end, so extend last (highest) interval or just ignore if inside current (using max)
        else:
            merged[-1][1] = max(merged[-1][1], end)

    # print(f"Merged ranges: {merged}")

    fresh_ids = 0
    for r in merged:
        fresh_ids += r[1] + 1 - r[0]
    print(f"Total fresh IDs: {fresh_ids}")
