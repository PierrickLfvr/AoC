import numpy as np

#Part 1

def part1():
    sum=0

    for line in open("inputs/4.txt"):
        winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
        numbers = [number for number in line.split(":")[1].split("|")[1].strip().split(" ") if number !='']
        matches = len(set(winning_numbers).intersection(set(numbers)))
        if matches > 0:
            sum+=pow(2, matches-1)
    print(f"Part 1: {sum}")

part1()

# Part 2

def part2():
    cards = np.ones(len(open("inputs/4.txt").readlines()))
    for i, line in enumerate(open("inputs/4.txt")):
        winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
        numbers = [number for number in line.split(":")[1].split("|")[1].strip().split(" ") if number !='']
        matches = len(set(winning_numbers).intersection(set(numbers)))
        if matches > 0:
            for j in range(matches):
                cards[i+j+1] += cards[i]
    print(f"Part 2: {int(cards.sum())}")

part2()
        
        