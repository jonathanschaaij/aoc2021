def parseInput():
    file= open("input.txt","r")
    out = []
    for line in file:
        line = line.strip()
        row = []
        for char in line:
            row.append(int(char))
        out.append(row)
    return out

def part1(field):
    points = []
    cord = []
    for y, row in enumerate(field):
        for x, num in enumerate(row):
            if y != 0:
                if field[y - 1][x] <= num:
                    continue
            if x != 0:
                if field[y][x - 1] <= num:
                    continue
            if x != len(row) - 1:
                if field[y][x + 1] <= num:
                    continue
            if y != len(field) - 1:
                if field[y + 1][x] <= num:
                    continue
            points.append(num)
            cord.append([x, y])

    risk = len(points) + sum(points)
    return risk, cord


def findUnique(arr):
    out = []
    for a in arr:
        if a not in out:
            out.append(a)
    return out

def findLarger(field, x, y):
    count = [[x,y]]
    num = field[y][x]
    print(num, end="")
    if y != 0:
        if 9 > field[y - 1][x] > num:
            count += findLarger(field, x, y - 1)
    if x != 0:
        if 9 > field[y][x - 1] > num:
            count += findLarger(field, x - 1, y)
    if x != len(field[0]) - 1:
        if 9 > field[y][x + 1] > num:
            count += findLarger(field, x + 1, y)
    if y != len(field) - 1:
        if 9 > field[y + 1][x] > num:
            count += findLarger(field, x, y + 1)
    return findUnique(count)
    
def part2(field, cord):
    basinSizes = []
    for lowPoint in cord:
        print(lowPoint)
        basinSizes.append(len(findLarger(field, lowPoint[0], lowPoint[1])))
        print("\n",basinSizes[-1])
        print()
    print(basinSizes)
    out = 1
    for i in range(3):
        out *= max(basinSizes)
        basinSizes.remove(max(basinSizes))
    return out


def main():
    field = parseInput()
    risk, cord = part1(field)
    print(part2(field, cord))

if __name__ == "__main__":
    main()
