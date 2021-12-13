#!/usr/bin/python3
import sys
from copy import deepcopy

def parseInput(filename, verbose=True):
    if verbose: print("-------------------- Reading input:  --------------------")
    file = open(filename, "r")
    out = []
    folds = []
    readDots = True
    for line in file:
        line = line.strip()
        if line == "":
            readDots = False
            continue
        if readDots:
            pos = line.split(",")
            out.append((int(pos[0]), int(pos[1])))
        else:
            inst = line.split("=")
            folds.append((inst[0][-1], int(inst[1])))
    file.close()
    if verbose: print("Finished Reading Input File")
    return out, folds

def createField(dots):
    maxX = maxY = 0
    for pos in dots:
        if pos[0] > maxX:
            maxX = pos[0]
        if pos[1] > maxY:
            maxY = pos[1]
    field = []
    for y in range(maxY + 1):
        row = []
        for x in range(maxX + 1):
            row.append(False)
        field.append(row)
    for pos in dots:
        field[pos[1]][pos[0]]= True
    return field

def foldX(field, X):
    newField = []
    for row in field:
        newRow = []
        for x, dot in enumerate(row):
            if x >= X:
                break
            mirrorX = 2 * X - x
            if mirrorX >= len(row):
                newRow.append(dot)
                continue
            newRow.append(dot or row[mirrorX])
        newField.append(newRow)
    return newField

def foldY(field, Y):
    newField = []
    for y, row in enumerate(field):
        if y >= Y:
            break
        newRow = []
        mirrorY = 2 * Y - y
        if mirrorY >= len(field):
            newField.append(row)
            continue
        for x, dot in enumerate(row): 
            newRow.append(dot or field[mirrorY][x])
        newField.append(newRow)
    return newField

def renderField(field):
    for line in field:
        for char in line:
            print("#" if char else " ", end="")
        print()
    print()

def part1(data, folds):
    print("-------------------- Starting Part1: --------------------")
    res = 0
    field = createField(data)
    # renderField(field)
    for fold in folds:
        if fold[0] == "x":
            field = foldX(field, fold[1])
        if fold[0] == "y":
            field = foldY(field, fold[1])
        break
    for row in field:
        res += sum(row)
    print("Finished part 1")
    print("Result: ", res)

def part2(data, folds):
    print("-------------------- Starting Part2: --------------------")
    res = 0
    field = createField(data)
    for fold in folds:
        if fold[0] == "x":
            field = foldX(field, fold[1])
        if fold[0] == "y":
            field = foldY(field, fold[1])
    renderField(field)
    print("Finished part 2")
    print("Result: ", res)

def main(filename):
    data, folds = parseInput(filename)
    part1(data, folds)
    part2(data, folds)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Please specify the filename of the input data")
