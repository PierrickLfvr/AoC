import numpy as np


# Part 1
def part1():
    sum = 0
    for line in open("inputs/1.txt"):
        #use regex to find first and last digit of the string
        digits = np.array([int(d) for d in line if d.isdigit()])
        sum+=digits[0]*10+digits[-1]
    print(f"Part 1: {sum}")
part1()


# Part 2
def find_digits(string):
    digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    first_digit = None
    last_digit = None
    start=""
    end=""
    i=0
    while not (first_digit and last_digit) and i<len(string):
        if not first_digit:
            if string[i].isdigit():
                first_digit = string[i]
            else:
                start += string[i]
                for digit in digit_mapping:
                    if digit in start:
                        first_digit = digit_mapping[digit]
        if not last_digit:
            current = string[-1-i]
            if current.isdigit():
                last_digit = current
            else:
                end = current + end
                for digit in digit_mapping:
                    if digit in end:
                        last_digit = digit_mapping[digit]
        i+=1
    return int(first_digit+last_digit)

def part2():
    sum = 0
    for line in open("inputs/1.txt"):
        #replace spelled out numbers with digits
        corrected_line = find_digits(line)
        sum+=corrected_line

    print(f"Part 2: {sum}")
part2()