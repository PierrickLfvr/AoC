
#Part 1

class Bin:
    def __init__(self, bin):
        self.start = bin[1]
        self.end = bin[1]+bin[2]-1
        self.value = bin[0]-bin[1]

    def apply(self, i):
        if i >= self.start and i <= self.end:
            return self.value + i
        else:
            return i
        
    def __str__(self):
        return f"Bin({self.start},{self.end},{self.value})"
    
    def __lt__(self, other):
        return self.start < other.start

maps = []
i=-1
for line in open('inputs/5.txt'):
    if line.startswith('seeds: '):
        seeds = list(map(int, line.strip().split(' ')[1:]))
    elif line[0].isalpha():
        maps.append([])
        i+=1
    elif line[0].isdigit():
        maps[i].append(Bin(list(map(int, line.strip().split(' ')))))

def part1():
    mini = 9999999999
    for seed in seeds:
        location = seed
        for i in range(len(maps)):
            for bin in maps[i]:
                location = bin.apply(seed)
                if location != seed:
                    seed = location
                    break
        mini = min(mini, location)
    print(f"Part 1: {mini}")

part1()

#Part 2

class Seeds:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def part2():
    mini = 9999999999
    sorted_maps = [sorted(map) for map in maps]
    
    for i in range(len(seeds)//2):
        start = seeds[i*2]
        end = seeds[i*2]+seeds[i*2+1]-1
        next_queue = [Seeds(start, end)]
        
        for k, step in enumerate(sorted_maps):
            
            queue = next_queue.copy()
            next_queue = []
            
            while len(queue) > 0 :
                seed = queue.pop(0)

                for j,bin in enumerate(step):
                    if seed.end < bin.start:
                        next_queue.append(seed)
                        break
                    
                    #seeds start before the bin
                    elif seed.start < bin.start: 
                        next_queue.append(Seeds(seed.start, bin.start-1))
                        if seed.end <= bin.end:
                            next_queue.append(Seeds(bin.start+bin.value, seed.end+bin.value))
                        else:
                            next_queue.append(Seeds(bin.start+bin.value, bin.end+bin.value))
                            queue.append(Seeds(bin.end+1, seed.end))
                        break
                        
                    #seeds start in the middle of bin
                    elif seed.start < bin.end:
                        if seed.end <= bin.end:
                            next_queue.append(Seeds(seed.start+bin.value, seed.end+bin.value))
                        else:
                            next_queue.append(Seeds(seed.start+bin.value, bin.end+bin.value))
                            queue.append(Seeds(bin.end+1, seed.end))
                        break
                    
                    else:
                        if j == len(step)-1:
                            next_queue.append(seed)  
                           
        mini = min(mini, min([seed.start for seed in next_queue]))
    print(f"Part 2: {mini}")

part2()
