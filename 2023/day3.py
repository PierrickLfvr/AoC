import numpy as np
import string

#Parsing the input
grid = []
for line in open("inputs/3.txt"):
    grid.append(line.strip())

#Part 1
def has_neighbors(x, y, grid):
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i==0 and j==0):
                if x+i < 0 or x+i >= len(grid) or y+j < 0 or y+j >= len(grid[0]):
                    continue
                if grid[x+i][y+j] != "." and grid[x+i][y+j] in string.punctuation:
                    return True
    return False
        
def part1():
    sum = 0
    is_valid = False
    curr_number = ""

    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char.isdigit():
                is_valid += has_neighbors(x, y, grid)
                curr_number += char
            elif curr_number != "":
                if is_valid:
                    sum+=int(curr_number)
                curr_number = ""
                is_valid = False

    print(f"Part 1: {sum}")

part1()

# Part 2
def get_number(x, y, grid):
    number=grid[x][y]
    min_y = y
    if y+1<len(grid[0]) and grid[x][y+1].isdigit():
        number+=grid[x][y+1]
        if y+2<len(grid[0]) and grid[x][y+2].isdigit():
            number+=grid[x][y+2]
    if y-1>=0 and grid[x][y-1].isdigit():
        number = grid[x][y-1] + number
        min_y = y-1
        if y-2>=0 and grid[x][y-2].isdigit():
            number = grid[x][y-2] + number
            min_y = y-2
    origin = x, min_y
    return origin, int(number)

def check_gear(x, y, grid):
    numbers=[]
    origins = []
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i==0 and j==0):
                if x+i < 0 or x+i >= len(grid) or y+j < 0 or y+j >= len(grid[0]):
                    continue
                if grid[x+i][y+j].isdigit():
                    origin, number = get_number(x+i, y+j, grid)
                    if origin not in origins:
                        origins.append(origin)
                        numbers.append(number)
    if len(numbers) == 2:
        return np.prod(numbers)
    return 0

def part2():
    sum=0
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "*":
                sum+=check_gear(x, y, grid)

    print(f"Part 2: {sum}")
part2()