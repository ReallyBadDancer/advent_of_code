import sys

test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
test_data = test_data.split("\n")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
digits = [str(i) for i in digits]
string_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
digits = digits + string_digits
print(digits)

with open("cal_data") as ifile:
    cal_data = ifile.readlines()

print(cal_data)

# Strip all of the newline characters from the cal data
test = False  # If using the test data from the description.
cal_data = [i.strip() for i in cal_data] if not test else test_data
print("Raw Calibration Data:")
print(cal_data)

# cal_data_digits = []
# for line in cal_data:
#     curr_digits = []
#     for character in line:
#         if character in digits:
#             curr_digits.append(character)
#     cal_data_digits.append(curr_digits)
#
# for inx, line in enumerate(cal_data_digits):
#     cal_data_digits[inx] = int(line[0] + line[-1])
#
# answer1 = sum(cal_data_digits)
# print(cal_data_digits)
# print(answer1)

# Part 2
print("--------------\nStart Part 2:\n--------------")

# Create a dictionary mapping spelled numbers to digit numbers.
zipped_digits = zip(string_digits, digits)
unzipped_tuples = []
for dig in zipped_digits:
    unzipped_tuples.append(dig)
dig_dict = dict(unzipped_tuples)
print("dig_dict", dig_dict)

results = []
for line in cal_data:
    print(f"Searching {line}")
    curr_line = ""
    while len(line) > 0:
        for dig in digits:  # Search all word and numeric numbers
            if line.removeprefix(dig) != line:  # This is how I test if the first part of the string is a number.
                if dig in dig_dict:  # If it's a "word" number
                    curr_line += dig_dict[dig]  # Add the number itself to the current line string
                    line = line[1:]  # Cut off the first character to resume search of the line
                    break  # Break out of the digits loop to start searching the next character.
                else:
                    curr_line += dig  # If it's just a number, add it to current string
                    line = line[1:]
                    break
        else:
            line = line[1:]  # Didn't find a number here, just cut off the first character and resume search.
    results.append(curr_line)  # String is consumed (length 0) so add this to the results list and move to next line.

print("Verbose Results:", results)
for inx, line in enumerate(results):  # Keep only the first and last character of each result. Convert them to integers.
    results[inx] = int(line[0] + line[-1])
print("Final Results:", results)
print(sum(results))  # Sum all results and print out the final answer.
