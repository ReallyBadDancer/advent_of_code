import aoc_utils
from operator import lt, gt, eq

data = aoc_utils.import_data_as_lines(example=False)
print(data)

data = [d.split(" ") for d in data]
print(data)

int_reports = []
for d in data:
    int_reports.append([int(i) for i in d])
data = int_reports
print(data)


def safety_check(report: list):
    if report[0] == report[1]:
        print(f"Equal! {report[0]}")
        return 0
    elif report[1] > report[0]:
        sign = gt
        margin = 3
    else:
        sign = lt
        margin = -3

    for inx, level in zip(range(len(report)-1), report):
        if eq(report[inx+1], report[inx]):
            print(f"Equal! {report[inx]}")
            return 0
        elif sign(report[inx+1], report[inx]):
            print(f"Correct Direction! {report[inx]}")
            if sign(report[inx+1] - margin, report[inx]):
                print("...but by too much!")
                return 0
        else:
            print(f"Wrong Direction! {report[inx]}")
            return 0
    print("Report is GOOD!")
    return 1

total = 0
for report in data:
    total += safety_check(report)

print(total)







