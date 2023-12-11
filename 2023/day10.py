import numpy as np
#Preprocessing
grid = []
start = None
for i, line in enumerate(open('inputs/10.txt')):
    grid.append([c for c in line.strip()])
    if not start and "S" in line:
        start = (i, line.strip().index("S"))
#print(np.array(grid))
#print(start)

def get_starting_directions(grid, start):
    directions = []
    i, j = start
    if i+1 < len(grid) and (grid[i+1][j] == "|" or grid[i+1][j] == "L" or grid[i+1][j] == "J"):
        directions.append((i+1, j))
    if i-1 >= 0 and (grid[i-1][j] == "|" or grid[i-1][j] == "7" or grid[i-1][j] == "F"):
        directions.append((i-1, j))
    if j+1 < len(grid[0]) and (grid[i][j+1] == "-" or grid[i][j+1] == "J" or grid[i][j+1] == "7"):
        directions.append((i, j+1))
    if j-1 >= 0 and (grid[i][j-1] == "-" or grid[i][j-1] == "L" or grid[i][j-1] == "F"):
        directions.append((i, j-1))
    return directions

def get_next_direction(grid, current, previous):
    i, j = current
    shape = grid[i][j]
    if shape == "|":
        return (i+1,j) if previous[0] < i else (i-1, j)
    elif shape == "-":
        return (i, j+1) if previous[1] < j else (i, j-1)
    elif shape == "L":
        return (i, j+1) if j == previous[1] else (i-1, j)
    elif shape == "F":
        return (i, j+1) if j == previous[1] else (i+1, j)
    elif shape == "7":
        return (i, j-1) if j == previous[1] else (i+1, j)
    elif shape == "J":
        return (i, j-1) if j == previous[1] else (i-1, j)
    else:
        return None

grid2=np.zeros(np.shape(grid), dtype=str)
#Part 1
def part1():
    directions_to_explore = get_starting_directions(grid, start)

    current_pos = directions_to_explore[0]
    previous_pos = start

    i = 1
    while current_pos != start:
        grid2[current_pos[0], current_pos[1]] = grid[current_pos[0]][current_pos[1]]
        next_pos = get_next_direction(grid, current_pos, previous_pos)
        previous_pos = current_pos
        current_pos = next_pos
        #print("going to ", current_pos)
        #print("from ", previous_pos)
        i+=1
    print(f'Part 1: {i//2}')

part1()
grid2[start[0], start[1]] = "S"
#replace '' with '.' in grid2
grid2[grid2==''] = '*'
#print(grid2)

def fill_grid(grid, start, direction):
    i, j = start
    k,l=direction
    next_pos = (i+k, j+l)
    if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
        return
    elif grid[next_pos[0]][next_pos[1]] == '*':
        grid[next_pos[0]][next_pos[1]] = '1'
        fill_grid(grid, next_pos, direction)


#Part 2
def part2():
    directions_to_explore = get_starting_directions(grid, start)

    current_pos = directions_to_explore[0]
    previous_pos = start
    direction = (0, 1)
    #print(grid[current_pos[0]][current_pos[1]])
    while current_pos != start:
        fill_grid(grid2, current_pos, direction)
        if grid[current_pos[0]][current_pos[1]] == 'L':
            direction = (-direction[1], -direction[0])
        elif grid[current_pos[0]][current_pos[1]] == 'F':
            direction = (direction[1], direction[0])
        elif grid[current_pos[0]][current_pos[1]] == '7':
            direction = (-direction[1], -direction[0])
        elif grid[current_pos[0]][current_pos[1]] == 'J':
            direction = (direction[1], direction[0])
        fill_grid(grid2, current_pos, direction)
        next_pos = get_next_direction(grid, current_pos, previous_pos)
        previous_pos = current_pos
        current_pos = next_pos
        #print("going to ", current_pos)
        #print("from ", previous_pos)
    #count number of 1s
    print(f'Part 2: {np.sum(grid2=="1")}')
    
part2()

