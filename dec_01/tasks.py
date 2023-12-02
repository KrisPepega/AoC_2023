import re


# task_1
file_str = open("input.txt", "r").read()
filtered_file = re.sub("[^0-9-\\s]", "", file_str)
sum = 0
for ln in filtered_file.splitlines():
    sum += int(ln[0] + ln[-1])
print(sum)


# task_2
file_str = open("input.txt", "r").read()
numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


sum = 0
for ln in file_str.splitlines():
    first = ""
    last = ""
    r = len(ln) - 1

    for i, c in enumerate(ln):
        if first.isdigit() and last.isdigit():
            break

        if c.isdigit() and first.isalpha():
            first = c
        elif first.isdigit() != True:
            first += c

        if ln[r - i].isdigit() and last.isalpha():
            last = ln[r - i]
        elif last.isdigit() != True:
            last = ln[r - i] + last

        if len(first) >= 3 or len(last) >= 3:
            for k in list(numbers_dict.keys()):
                if k in first:
                    first = numbers_dict[k]
                if k in last:
                    last = numbers_dict[k]

    sum += int(first + last)
print(sum)
