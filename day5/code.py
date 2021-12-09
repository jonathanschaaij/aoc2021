def parseInput():
    file = open("input.txt", "r")
    size = [0,0]
    rules = []
    for line in file:
        line = line.strip()
        parts = line.split(" -> ")
        rule = []
        for i, part in enumerate(parts):
            rule.append([int(a) for a in part.split(",")])
            if rule[i][0] > size[0]:
                size[0] = rule[i][0]
            if rule[i][1] > size[1]:
                size[1] = rule[i][1]
        rules.append(rule)
    return rules, size

def renderSpace(space):
    for row in space:
        for item in row:
            if item == 0:
                print(".", end="")
            else:
                print(item, end="")
        print()

def sumSpace(space):
    out = 0
    for row in space:
        for num in row:
            if num > 1:
                out += 1
    return out

def diff(A):
    return max(A)+1 - min(A)
def rising(a):
    return a[0] < a[1]

def main():
    rules, size = parseInput()
    r = [0] * (size[0]+1)
    space = list(map(list,[r] * (size[1]+1)))
    for rule in rules:
        X = [rule[0][0], rule[1][0]]
        Y = [rule[0][1], rule[1][1]]
        X2 = list(range(min(X), min(X) + diff(X)))
        Y2 = list(range(min(Y), min(Y)+ diff(Y)))
        if len(X2) == 1:
            for y in Y2:
                space[y][X2[0]] += 1
        elif len(Y2) == 1:
            for x in X2:
                space[Y2[0]][x] += 1
        else:
            if rising(X) != rising(Y):
                Y2.reverse()
            for i, x in enumerate(X2):
                space[Y2[i]][x]+=1


    renderSpace(space)
    print(sumSpace(space))

if __name__ == "__main__":
    main()
