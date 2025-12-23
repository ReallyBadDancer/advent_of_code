def import_data_as_string(example=True):
    print("\nImporting raw data as string:")
    ifilename = "example_input" if example else "puzzle_input"
    with open(ifilename) as ifile:
        data = ifile.read()
    return data


def import_data_as_lines(example=True):
    print("\nImporting raw data as lines:")
    ifilename = "example_input" if example else "puzzle_input"
    with open(ifilename) as ifile:
        data = ifile.readlines()
        data = [d.strip() for d in data]
    return data
