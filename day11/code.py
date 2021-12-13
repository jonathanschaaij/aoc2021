#!/usr/bin/python3
import sys

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

def flash(oldField, pos):
    field = []
    for row in oldField:
        field.append(row[:])
    field[pos[0]][pos[1]] = 11
    adj = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    for side in adj:
        Y = pos[0] + side[1]
        X = pos[1] + side[0]
        if Y < 0 or Y >= len(field):
            continue
        if X < 0 or X >= len(field[0]):
            continue
        if field[Y][X] < 10:
            field[Y][X] += 1
    return field

def render(field):
    for row in field:
        for char in row:
            print(char, end="")
        print()

def addEnergy(field):
    out = []
    for row in field:
        newRow = []
        for num in row:
            newRow.append(num%10 + 1)
        out.append(newRow)
    return out

def resetFlashes(field):
    out = []
    for row in field:
        newRow = []
        for num in row:
            newRow.append(num if num < 10 else 0)
        out.append(newRow)
    return out

def indexFlash(field):
    for y, row in enumerate(field):
        if 10 in row: return (y,row.index(10))
    return False

def part1(field):
    print("-------------------- Starting Part1: --------------------")
    res = 0
    for step in range(100):
        field = addEnergy(field)
        while True:
            pos = indexFlash(field)
            if not bool(pos):
                break
            res += 1
            field = flash(field, pos)
        field = resetFlashes(field)
        print("Step: ", step)
        render(field)
        print("\n")
    print("Finished part 1")
    print("Result: ", res)

def part2(field):
    print("-------------------- Starting Part2: --------------------")
    step = 0
    size = len(field[0])*len(field)
    while True:
        step += 1
        count = 0
        field = addEnergy(field)
        while True:
            pos = indexFlash(field)
            if not bool(pos):
                break
            count += 1
            field = flash(field, pos)
        field = resetFlashes(field)
        # print("Step: ", step)
        # render(field)
        # print("\n")
        if count == size:
            break

    print("Finished part 2")
    print("Result: ", step)

def main(filename):
    data = parseInput(filename)
    part1(data)
    part2(data)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Please specify the filename of the input data")
