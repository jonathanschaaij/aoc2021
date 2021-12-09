def parseInput(filename):
    file = open(filename,"r")
    line = file.readline()
    line = line.strip()
    num = [int(a) for a in line.split(",")]
    file.close()
    return num

def nextDay(num):
    out = []
    for n in num:
        if n <= 0:
            out.append(8)
            out.append(6)
        else:
            out.append(n-1)
    return out

def part1(num):
    for x in range(80):
        num = nextDay(num)
        if x == 17:
            print(len(num))
    print(len(num))

def part2(num):
    left = [0]*9
    for i in num:
        left[i] += 1
    print(left)
    for day in range(256):
        a = left[0]
        left = left[1:]
        left[6] += a
        left.append(a)
    print(sum(left))

def main():
    num = parseInput("input.txt")
    part2(num)


if __name__ == "__main__":
    main()
