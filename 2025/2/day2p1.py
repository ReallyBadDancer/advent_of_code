EXAMPLE = False

if __name__ == "__main__":
    ifilename = "example_input" if EXAMPLE else "puzzle_input"
    with open(ifilename, "r") as f:
        ranges = f.read().split(",")
    print("Unprocessed Ranges: ", ranges)

    # Process these ranges into tuples representing start and finish integer
    range_tuples = []
    for r in ranges:
        range_tuples.append(tuple(map(int, r.split("-"))))
    print("Found Ranges: ", range_tuples)

    # Expand all ranges into a list of all product IDs and concatenate them
    prod_ids = []
    for r in range_tuples:
        for i in range(r[0], r[1]+1):
            prod_ids.append(i)
    print("Got Product IDs:", prod_ids)

    # Convert all IDs into strings
    prod_ids = map(str, prod_ids)

    # Drop all IDs with an odd number of digits
    print("Dropping all IDs with odd num of digits:")
    prod_ids = list(filter(lambda x: len(x) % 2 == 0 , prod_ids))
    print("Got Product IDs:", prod_ids)

    # Create another list of tuples with the ID split in half
    print("Getting split ID strings:")
    prod_id_tuples = [(i[:len(i)//2], i[len(i)//2:]) for i in prod_ids]
    print("Got Product IDs: ", prod_id_tuples)

    # Drop all IDs with two identical elements, then recombine
    print("Keeping silly IDs:")
    prod_id_tuples = list(filter(lambda x: x[0] == x[1], prod_id_tuples))
    prod_ids = [int(i[0]+i[1]) for i in prod_id_tuples]
    print("Got Product IDs: ", prod_ids)

    #Sum together all silly IDs
    print("Summing the silly IDs:")
    print(sum(prod_ids))
