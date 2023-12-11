times = []
distances = []
for line in open('inputs/6.txt'):
    if times == []:
        times = [int(digit) for digit in line.strip().split(':')[1].split(" ") if digit!='']
    else:
        distances = [int(digit) for digit in line.strip().split(':')[1].split(" ") if digit!='']

def quick_maths(time, distance, speed=1):
    racine = (-time*speed-(((time*speed)**2) - 4*distance)**0.5)/-2
    return 2 * (int(racine) if not racine.is_integer() else int(racine) -1) - time+1

#Part 1
def part1():
    sum=1
    for distance,time in zip(distances, times):
        sum*=quick_maths(time, distance)
    print(f"Part 1: {sum}")

part1()

#Part 2

time = ""
distance = ""
for d, t in zip(distances,times):
    time+=str(t)
    distance+=str(d)
time = int(time)
distance = int(distance)

def part2():
    print(f"Part 2: {quick_maths(time, distance)}")
part2()
