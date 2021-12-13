#!/usr/bin/python3
import sys

def parseInput(filename, verbose=True):
    if verbose: print("-------------------- Reading input:  --------------------")
    file = open(filename, "r")
    out = []
    chars = ["(","[","{","<",">","}","]",")"]
    for line in file:
        line = line.strip()
        row = []
        for char in line:
            row.append(chars.index(char))
        out.append(row)
    file.close()
    if verbose: print("Finished Reading Input File")
    return out

def part1(data):
    print("-------------------- Starting Part1: --------------------")
    wrong = []
    for row in data:
        opened = []
        for char in row:
                if char < 4:
                    opened.append(char)
                else:
                    if len(opened) == 0:
                        wrong.append(char)
                        break
                    elif char + opened[-1] != 7:
                        wrong.append(char)
                        break
                    else: opened = opened[:-1]
    res = 0
    for x in wrong:
        if x == 7: res += 3
        elif x == 6: res += 57
        elif x == 5: res += 1197
        elif x == 4: res += 25137
    print("Finished part 1")
    print("Result: ", res)

def part2(data):
    print("-------------------- Starting Part2: --------------------")
    res = []
    for row in data:
        opened = []
        for char in row:
                if char < 4:
                    opened.append(char)
                else:
                    if len(opened) == 0:
                        break
                    elif char + opened[-1] != 7:
                        break
                    else: opened = opened[:-1]
        else:
            rowRes = 0
            while len(opened) != 0:
                rowRes *= 5
                rowRes += opened[-1] + 1
                opened = opened[:-1]
            res.append(rowRes)
            print("RowRes: ", rowRes)
    res.sort()
    res = res[int(len(res)/2)]
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
