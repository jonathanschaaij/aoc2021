#!/usr/bin/python3
from copy import deepcopy
import sys

def parseInput(filename, verbose=True):
    if verbose: print("-------------------- Reading input:  --------------------")
    file = open(filename, "r")
    out = []
    testSection = {}
    for line in file:
        line = line.strip()
        if line == "":
            out.append(testSection)
            testSection = {}
            continue
        parts = line.split("-")
        for i in range(2):
            if parts[i] not in testSection.keys():
                testSection[parts[i]] = []
            testSection[parts[i]].append(parts[i - 1])
    out.append(testSection)
    file.close()
    if verbose: print("Finished Reading Input File")
    return out

def findPaths(data, start, end, done, doTwice="?"):
    out = 0
    done = deepcopy(done)
    done.append(start.lower())
    # print("Start:",start,"\nend:",end,"\ndone:", done,"\n")
    if start == end:
        if doTwice != "":
            if done.count(doTwice) != 2:
                return 0
        # print("Valid:", done)
        return 1
    for x in data[start]:
        if x == "start":
            continue
        if x in done and x != doTwice:
            continue
        if done.count(x) == 2:
            continue
        out += findPaths(data, x, end, done, doTwice)
        if doTwice == "":
            out += findPaths(data, x, end, done, x)
    return out

def part1(data):
    print("-------------------- Starting Part1: --------------------")
    for i, test in enumerate(data):
        print("File: ", i + 1)
        print(test)
        out = findPaths(test, "start", "end", [])
        print(out)
        print()
    print("Finished part 1")
    # print("Result: ", res)

def part2(data):
    print("-------------------- Starting Part2: --------------------")
    for i, test in enumerate(data):
        print("File: ", i + 1)
        print(test)
        out = findPaths(test, "start", "end", [], "")
        print(out)
        print()
    print("Finished part 2")

def main(filename):
    data = parseInput(filename)
    part1(data)
    part2(data)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Please specify the filename of the input data")
