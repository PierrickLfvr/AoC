import numpy as np
#Preprocessing

data = []
for line in open('inputs/9.txt'):
    data.append([int(d) for d in line.strip().split(" ")])

data_np = np.array(data)

def recursive_derivate(data):
    deriv = data[1:] - data[:-1]
    if np.all(deriv == 0):
        return data[-1]
    else:
        return data[-1] + recursive_derivate(deriv)
    
#Part 1
def part1():
    sum=0
    for d in data:
        sum+=recursive_derivate(np.array(d))
    print(f"Part 1: {sum}")

part1()

#Part 2

def other_recursive_derivate(data):
    deriv = data[1:] - data[:-1]
    if np.all(deriv == 0):
        return data[0]
    else:
        return data[0] - other_recursive_derivate(deriv)
    
def part2():
    sum=0
    for d in data:
        sum+=other_recursive_derivate(np.array(d))
    print(f"Part 2: {sum}")
part2()