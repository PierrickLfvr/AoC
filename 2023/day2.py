#Part 1
limits = {"red":12, "green":13, "blue":14}

def part1():
    sum=0
    for line in open("inputs/2.txt"):
        id = int(line.split(":")[0].split(" ")[1])
        unvalid = False
        for round in line.split(":")[1].split(";"):
            if unvalid:
                break
            for grab in round.split(","):

                digit, color = grab[1:].split(" ")

                if int(digit) > limits[color.strip()]:
                    unvalid = True
        if not unvalid:
            sum+=id
    print(f'Part 1: {sum}')
part1()

# Part 2

class GrabCounter():

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def add(self, color, digit):
        if color == "red":
            self.red = max(self.red, digit)
        elif color == "green":
            self.green = max(self.green, digit)
        elif color == "blue":
            self.blue = max(self.blue, digit)

    def get_power(self):
        return self.red * self.green * self.blue

def part2():
    sum=0
    for line in open("inputs/2.txt"):
        grabCounter = GrabCounter()
        for round in line.split(":")[1].split(";"):
            for grab in round.split(","):
                digit, color = grab[1:].split(" ")
                grabCounter.add(color.strip(), int(digit))
        sum+=grabCounter.get_power()
        
    print(f'Part 2: {sum}')

part2()