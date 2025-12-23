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

    invalid_ids = []
    # Create a dictionary with the ID as key
    for prod_id in prod_ids:
        for i in range(1,len(prod_id)+1):
            # Break loop if past the halfway point of the id.
            if i > len(prod_id)/2:
                break
            # Create a token that could be repeated
            token = prod_id[:i]
            # Create a possible silly_id from the token
            silly_id = token * int(len(prod_id)/len(token))
            # print("PID: ", prod_id, "\nSID: ", silly_id)
            if silly_id == prod_id:
                # print("Got Invalid ID: ", prod_id)
                invalid_ids.append(prod_id)
                break

    invalid_ids = list(map(int, invalid_ids))
    print("Got Invalid IDs: ", invalid_ids)
    print("Sum of Invalid IDs: ", sum(invalid_ids))











    # Create empty list silly_ids
    # For each ID, compare each sequence in the value slice by slice to the ID
    # If each slice matches, then add to silly_ids.
