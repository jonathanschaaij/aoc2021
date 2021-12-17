#!/usr/bin/python3
import sys
import timeit
from copy import deepcopy

def parseInput(filename):
    print("---------- Reading input:  ----------")
    file = open(filename, "r")
    out = []
    for line in file:
        line = line.strip()
        line = line[line.index(":")+2:]
        sections = line.split(", ")
        for coord in sections:
            nums = coord.split("=")
            vals = nums[1].split("..")
            out.append([int(a) for a in vals])
    file.close()
    print("Finished Reading Input File")
    return out

def nextState(pos, vel, target):
    pos[0] += vel[0]
    pos[1] += vel[1]
    vel[0] -= 1 if vel[0] > 0 else 0
    vel[1] -= 1
    return pos, vel

def simulate(initVel, target):
    pos = [0, 0]
    vel = initVel
    maxY = 0
    while True:
        pos, vel = nextState(pos, vel, target)
        if pos[1] > maxY: maxY = pos[1]
        if target[0][0] <= pos[0] <= target[0][1] and target[1][0] <= pos[1] <= target[1][1]:
            return maxY # inSide the target
        if pos[1] < target[1][0]:
            if abs(vel[1]) > abs(target[1][0] - target[1][1]):
                return -1
            else:
                return -1
        if pos[0] > target[0][1]: return -1

def part1(data):
    print("---------- Starting Part1: ----------")
    xVel = 1
    while sum(range(xVel + 1)) < data[0][0]:
        xVel += 1
    height = []
    yRange = data[1][0]-data[1][1]
    for yVel in range(xVel, 1000):
        height.append(simulate([xVel, yVel], data))
        if yVel < abs(2 * yRange): continue
        if sum(height[(yRange-2):]) <= 0: break
    maxY = xVel + height.index(max(height))
    print([xVel,maxY])
    res = max(height)
    print("Finished part 1")
    print("Result: ", res)
    return maxY

def part2(data, maxY):
    print("---------- Starting Part2: ----------")
    res = 0
    for x in range(0, data[0][1]+1):
        for y in range(data[1][0], maxY+1):
            if simulate([x, y], data) != -1:
                res +=1
    print("Finished part 2")
    print("Result: ", res)

def main(filename):
    data = parseInput(filename)
    start1 = timeit.default_timer()
    maxY = part1(data)
    start2 = timeit.default_timer()
    part2(data, maxY)
    end = timeit.default_timer()
    print("------------ Performance ------------")
    print("Time part1: ", start2 - start1)
    print("Time Part2: ", end - start2)

def output(*args):
    if not quiet:
        print("".join([str(a) for a in args]))

if __name__ == "__main__":
    quiet = False
    if len(sys.argv) >= 3:
        quiet = ("q" in sys.argv[1])
    if len(sys.argv) >= 2:
        main(sys.argv[-1])
    else:
        print("Please specify the filename of the input data")
