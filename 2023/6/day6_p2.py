test = False
ifilename = "example_input" if test else "puzzle_input"

print("\nImport Raw data:")
with open(ifilename) as ifile:
    data = ifile.read()
print(data)
print("\nConvert raw data into single large time and distance integer")
data = data.splitlines()
print(data)
data = [int(line.split(":")[1].replace(" ","")) for line in data]
print("Time/Distance Data a blobbed integer: ", data)

print("\nDetermine how long we must press the button to win the race: ")
race_duration, best_distance = data
winning_press_times = 0
for t in range(1, race_duration+1):
    print(f"Processing {t} of {race_duration}")
    speed = t
    run_duration = race_duration - t
    distance = speed * run_duration
    if distance > best_distance:
        winning_press_times += 1

print("Part 2 solution: ", winning_press_times)
