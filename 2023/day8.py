import math

#Preprocess

instructions = []
places = {}
instructions_map = {"L":0, "R":1}

for line in open('inputs/8.txt'):
    if len(instructions) == 0:
        instructions = [instructions_map[letter] for letter in line.strip()]
    elif line!="\n":
        origin, destinations = line.strip().split(" = ")
        places[origin] = destinations[1:-1].split(", ")

#Part 1
def part1():
    step = 0
    current_loc = "AAA"
    destination = "ZZZ"
    while current_loc != destination:
        current_loc = places[current_loc][instructions[step%len(instructions)]]
        step+=1


    print(f"Part 1: {step}")
part1()

#Part 2

def part2():
    step = 0
    current_loc = [loc for loc in places.keys() if loc.endswith("A")]
    solutions = [0 for loc in current_loc]
    while 0 in solutions:
        for i,loc in enumerate(current_loc):
            current_loc[i] = places[loc][instructions[step%len(instructions)]]
            if current_loc[i].endswith("Z") and solutions[i] == 0:
                solutions[i] = step+1
        step+=1
    
    print(f"Part 2: { math.lcm(*solutions)}")
part2()