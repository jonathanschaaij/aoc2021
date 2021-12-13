#!/usr/bin/python3
import sys

def parseInput(filename, verbose=True):
    if verbose: print("-------------------- Reading input:  --------------------")
    file = open(filename, "r")
    out = []

    file.close()
    if verbose: print("Finished Reading Input File")
    return out

def part1(data):
    print("-------------------- Starting Part1: --------------------")
    res = 0
    print("Finished part 1")
    print("Result: ", res)

def part2(data):
    print("-------------------- Starting Part2: --------------------")
    res = 0
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
