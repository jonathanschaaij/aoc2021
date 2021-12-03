file = open("input", "r")

posX = 0
depth = 0
aim = 0
dirs = ["forward","up","down"]

for line in file:
    line = line.strip()
    part = line.split()
    n = int(part[1])
    d = dirs.index(part[0])
    if d == 0:
        posX += n
        depth += n*aim
    elif d == 1:
        aim -= n
    elif d == 2:
        aim += n

print(depth*posX)
