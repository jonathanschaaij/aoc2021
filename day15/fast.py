#!/usr/bin/python3
import sys
from copy import deepcopy

def parseInput(filename, verbose=True):
    if verbose: print("-------------------- Reading input:  --------------------")
    file = open(filename, "r")
    out = []
    for line in file:
        line = line.strip()
        row = []
        for char in line:
            row.append(int(char))
        out.append(row)
    file.close()
    if verbose: print("Finished Reading Input File")
    return out

def findPath(field):
    boundary = [[0, 0]]
    boundaryRisk = [0]
    end = [len(field[0]) - 1, len(field) - 1]
    print(end)
    risk = []
    for y in range(end[1]+1):
        row = []
        for x in range(end[0]+1):
            row.append(-1)
        risk.append(row)
    risk[0][0] = 0
    def getRisk(pos):
        x, y = pos
        return risk[y][x]
    def setRisk(pos, r):
        x, y = pos
        risk[y][x] = field[y][x] + r
        boundaryRisk.append(risk[y][x])
    while True:
        ind = boundaryRisk.index(min(boundaryRisk))
        boundaryRisk.pop(ind)
        pos = boundary.pop(ind)
        r = getRisk(pos)
        if pos == end:
            return getRisk(pos)
        if pos[0] < end[0]:
            newPos = [pos[0]+1, pos[1]]
            if getRisk(newPos) == -1:
                boundary.append(newPos)
                setRisk(newPos, r)
        if pos[1] < end[1]:
            newPos = [pos[0], pos[1] + 1]
            if getRisk(newPos) == -1:
                boundary.append(newPos)
                setRisk(newPos, r)
        if pos[1] > 0:
            newPos = [pos[0], pos[1] - 1]
            if getRisk(newPos) == -1:
                boundary.append(newPos)
                setRisk(newPos, r)
        if pos[0] > 0:
            newPos = [pos[0] -1, pos[1]]
            if getRisk(newPos) == -1:
                boundary.append(newPos)
                setRisk(newPos, r)

def render(field):
    for row in field:
        for char in row:
            print(char,"\t", end="")
        print()

def part1(data):
    print("-------------------- Starting Part1: --------------------")
    res = findPath(data)
    print("Finished part 1")
    print("Result: ", res)

def createLargeCave(field, n=5):
    out = []
    for i in range(n):
        for row in field:
            newRow = []
            for j in range(n):
                for num in row:
                    newNum = num + i + j
                    newRow.append(newNum) if newNum < 10 else newRow.append(newNum - 9)
            out.append(newRow)
    return out

def part2(data):
    print("-------------------- Starting Part2: --------------------")
    largeCave = createLargeCave(data, 5)
    # render(largeCave)
    res = findPath(largeCave)
    print("Finished part 2")
    print("Result: ", res)

def main(filename):
    data = parseInput(filename)
    part1(data)
    part2(data)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Please specify the filename of the input data")
