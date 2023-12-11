import numpy as np
#Preprocessing
grid = []
for line in open('inputs/11.txt'):
    grid.append([1 if c == "#" else 0 for c in line.strip()])

grid = np.array(grid)
grid2 = np.array(grid)
rows_to_insert = []
for i,line in enumerate(grid2):
    if line.sum() == 0:
        #insert line of zeros
        rows_to_insert.append(i)
for i, row in enumerate(rows_to_insert):
    grid2 = np.insert(grid2, row+i, np.zeros(len(grid2[0])), axis=0)

columns_to_insert = []
for i, column in enumerate(grid.T):
    if column.sum() == 0:
        columns_to_insert.append(i)
for i, column in enumerate(columns_to_insert):
    grid2 = np.insert(grid2, column+i, np.zeros(len(grid2)), axis=1)

#part 1

def part1():
    galaxies = []
    sum=0
    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            if grid2[i][j] == 1:
                galaxies.append([i,j])
    for galaxy in galaxies:
        for galaxy2 in galaxies:
            if galaxy != galaxy2:
                sum+=abs(galaxy[0]-galaxy2[0])+abs(galaxy[1]-galaxy2[1])
    print(f'Part 1: {sum//2}')
                
part1()

#part 2
def part2(expansion=1000000):
    galaxies = []
    sum=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                galaxies.append([i,j])
    for galaxy in galaxies:
        for galaxy2 in galaxies:
            if galaxy != galaxy2:
                dist = 0
                for l in range(min(galaxy[0], galaxy2[0])+1, max(galaxy[0], galaxy2[0])+1):
                    if l in rows_to_insert:
                        dist+=expansion
                    else:
                        dist+=1
                for m in range(min(galaxy[1], galaxy2[1])+1, max(galaxy[1], galaxy2[1])+1):
                    
                    if m in columns_to_insert:
                        dist+=expansion
                    else:
                        dist+=1
                    
                sum+=dist
    print(f'Part 2: {sum//2}')
part2()
