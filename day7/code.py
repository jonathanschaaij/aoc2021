def parseInput():
    file = open("test.txt","r")
    line = file.readline().strip()
    nums = [int(a) for a in line.split(",")]
    file.close()
    return nums

def part1(num):
    costs = []
    for pos in range(max(num)):
        cost = 0
        num.sort()
        for i, n in enumerate(num):
            cost += abs(n-pos)
        costs.append(cost)
    print(min(costs))
    print(costs.index(min(costs)))

def part2(num):
    costs = []
    price = [0]
    for i in range(1,max(num)):
        price.append(price[i-1] + i)
    for pos in range(1,max(num)-1):
        cost = 0
        num.sort()
        for i, n in enumerate(num):
            cost += price[abs(n-pos)]
        costs.append(cost)
    print(min(costs))
    print(costs.index(min(costs)))


def main():
    num = parseInput()
    part2(num)

if __name__ == "__main__":
    main()
