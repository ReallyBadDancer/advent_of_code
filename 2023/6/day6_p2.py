test = False
ifilename = "example_input" if test else "puzzle_input"

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.read()
print(data)

print("\nConvert raw data into time/distance pairs")
data = data.splitlines()
data = [list(map(int, line.split(":")[1].split())) for line in data]  # Creates a list of integers
print("Data as a list: ", data)
time_distance_pairs = list(zip(*data))
print("Data as time/distance pairs:", time_distance_pairs)

print("\nDetermine how long we must press the button to win the race: ")
winning_sets = []
for race_duration, best_distance in time_distance_pairs:
    winning_press_times = []
    for t in range(1, race_duration+1):
        speed = t
        run_duration = race_duration - t
        distance = speed * run_duration
        if distance > best_distance:
            winning_press_times.append(t)
    winning_sets.append(winning_press_times)
print("Winning Sets: ", winning_sets)

print("\nCalculate number of possible winning combinations:")

ways_to_win = 1
for s in winning_sets:
    ways_to_win *= len(s)

print("Part 1 solution: ", ways_to_win)




