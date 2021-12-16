#!/usr/bin/python3
import sys

def parseInput(filename, verbose=True):
    if verbose: print("-------------------- Reading input:  --------------------")
    file = open(filename, "r")
    out = ""
    for line in file:
        print("Hex:\t",line.strip())
        for char in line.strip():
            out += bin(int(char, 16))[2:].zfill(4)
        print("Bin:\t",out)
    file.close()
    if verbose: print("Finished Reading Input File")
    return out


def readPacket(binStr, pos=0):
    versions = []
    version = (int(binStr[pos:pos + 3], 2))
    print("Version: ", version)
    versions.append(version)
    packType = int(binStr[pos + 3:pos + 6], 2)
    print("Type: ", packType)
    pos = pos + 6
    if packType == 4:
        val, pos = readSubPacket(binStr, pos)
        print("InnerValue: ", val)
        return ([version], pos, val)
    else:
        pos += 1
        vals = []
        if binStr[pos-1] == "0":
            packLen = int(binStr[pos:pos + 15],2)
            print("Bits for packages:",packLen)
            pos += 15
            prevPos = pos
            while pos-prevPos <= packLen-5:
                newVer, pos, val = readPacket(binStr, pos)
                vals.append(val)
                versions += newVer
                print("POSITITON WHILE COUNTING BITS:", pos)
        else:
            nSubPack = int(binStr[pos:pos + 11],2)
            print("Inner Packages: ",nSubPack)
            pos += 11
            for i in range(nSubPack):
                newVer, pos, val = readPacket(binStr, pos)
                vals.append(val)
                versions += newVer
    if packType == 0:
        val = sum(vals)
    elif packType == 1:
        val = 1
        for n in vals:
            val *= n
    elif packType == 2:
        val = min(vals)
    elif packType == 3:
        val = max(vals)
    elif packType == 5:
        val = int(vals[0] > vals[1])
    elif packType == 6:
        val = int(vals[0] < vals[1])
    elif packType == 7:
        val = int(vals[0] == vals[1])
    print("Val: ", val)
    return (versions, pos, val)

def readSubPacket(binStr, pos):
    val = ""
    while True:
        val += binStr[pos + 1: pos + 5]
        pos += 5
        if binStr[pos-5] == "0": break
    return (int(val, 2), pos)


def part1(data):
    print("-------------------- Starting Part1: --------------------")
    pos = 0
    res = []
    while pos < len(data)-11:
        ver, pos, val = readPacket(data, pos)
        print("Val: ",val)
        res += ver
    res = sum(res)

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
