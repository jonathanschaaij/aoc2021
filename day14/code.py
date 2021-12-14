#!/usr/bin/python3
import sys
from copy import deepcopy

def parseInput(filename, verbose=True):
    if verbose: print("-------------------- Reading input:  --------------------")
    file = open(filename, "r")
    out = {}
    firstLine = True
    for line in file:
        line = line.strip()
        if line == "":
            firstLine = False
            continue
        if firstLine:
            start = line
            continue
        pair, insert = line.split(" -> ")
        out[pair] = insert
    file.close()
    if verbose: print("Finished Reading Input File")
    return out, start

def polymerization(word, rules, steps):
    word = list(word)
    for n in range(steps):
        i = 1
        while i < len(word):
            pair = word[i - 1:i + 1]
            pair = "".join(pair)
            x = rules[pair]
            word[i:i] = x
            i += 1 + len(x)
        # print("After Step ", n + 1)
        # print("".join(word))
    occ = {}
    for char in word:
        if char not in occ.keys():
            occ[char] = 1
        else:
            occ[char] += 1
    res = max(occ.values())-min(occ.values())
    return res, word

def part1(rules, start):
    print("-------------------- Starting Part1: --------------------")
    res, x = polymerization(start,rules,10)
    print("Finished part 1")
    print("Result: ", res)

def part2(rules, start):
    print("-------------------- Starting Part2: --------------------")
    word = list(start)
    occPairs = {}
    for key in rules:
        occPairs[key] = 0
    for i in range(len(word) - 1):
        occPairs["".join(word[i:i+2])] = 1
    for step in range(40):
        newPairs = deepcopy(occPairs)
        for key in newPairs:
            if occPairs[key] == 0: continue
            a = key[0] + rules[key]
            b = rules[key] + key[1]
            newPairs[key] -= occPairs[key]
            newPairs[a] += occPairs[key]
            newPairs[b] += occPairs[key]
        occPairs = newPairs
    occ = {}
    for pair in occPairs:
        if pair[1] not in occ:
            occ[pair[1]] = 0
        occ[pair[1]] += occPairs[pair]
    occ[word[0]] += 1
    res = max(occ.values())-min(occ.values())
    print("Finished part 2")
    print("Result: ", res)

def main(filename):
    rules, start = parseInput(filename)
    part1(rules, start)
    part2(rules, start)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Please specify the filename of the input data")
