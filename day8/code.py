def parseInput():
    file= open("input.txt","r")
    out = []
    for line in file:
        line = line.strip()
        a, b = line.split(" | ")
        row = []
        for x in [a, b]:
            part = []
            digitStrings = x.split(" ")
            for digitString in digitStrings:
                part.append(digitString)
            row.append(part)
        out.append(row)
    return out

def stringToNum(string, parts):
    if len(string) == 2:
        return 1
    elif len(string) == 3:
        return 7
    elif len(string) == 4:
        return 4
    elif len(string) == 7:
        return 8
    elif len(string) == 5:
        if parts[1] in string:
            return 5
        elif parts[5] in string:
            return 3
        else:
            return 2
    elif len(string) == 6:
        if parts[3] not in string:
            return 0
        elif parts[2] in string:
            return 9
        else:
            return 6
    else:
        print("ERROR")
        print(string, parts)
        return string

def part1(data):
    out = 0
    for row in data:
        for n in row[1]:
            if n in [1, 4, 7, 8]:
                out += 1
    return out

def part2(data):
    outputValues = []
    for row in data:
        parts = list(map(list,[["a","b","c","d","e","f","g",]]*7))
        found = [False]*10
        while not found[0]:
            for x in row[0]:
                if len(x) == 2 and not found[1]:
                    found[1] = True
                    for sec in [0, 1, 3, 4, 6]:
                        parts[sec].remove(x[0])
                        parts[sec].remove(x[1])
                    parts[2] = [x[0], x[1]]
                    parts[5] = [x[0], x[1]]
                elif len(x) == 4 and found[1] and not found[4]:
                    found[4] = True
                    new = []
                    for char in x:
                        if char not in parts[2]:
                            new.append(char)
                    for sec in [0, 4, 6]:
                        for char in new:
                            parts[sec].remove(char)
                    parts[1] = new
                    parts[3] = new
                elif len(x) == 3 and found[4] and not found[7]:
                    found[7] = True
                    for char in x:
                        if char not in parts[2]:
                            new = char
                            break
                    for sec in [4, 6]:
                        parts[sec].remove(new)
                    parts[0] = new
                elif len(x) == 6 and found[7] and not found[6]:
                    for char in parts[2]:
                        if char not in x:
                            found[6] = True
                            notnew = char
                    if found[6]:
                        parts[2] = notnew
                        parts[5] = parts[5][0] if parts[5][0] != notnew else parts[5][1]
                elif len(x) == 5 and found[6] and (not found[3] or not found[5]):
                    if (parts[2] in x and parts[5] in x) and not found[3]:
                        found[3] = True
                        for char in x:
                            if char not in [parts[0], parts[2], parts[5]] + parts[1]:
                                parts[6] = char
                                parts[4] = parts[4][0] if parts[4][0] != parts[6] else parts[4][1]
                elif len(x) == 6 and found[3] and not found[0]:
                    new = ""
                    for char in parts[1]:
                        if char in x:
                            if new == "":
                                new = char
                            else:
                                break
                    else:
                        found[0] = True
                        parts[1] = new
                        parts[3] = parts[3][1] if parts[3][1] != new else parts[3][0]
                        break
                elif found[0]:
                    break

        val = 0
        for d in row[1]:
            val = 10 * val + stringToNum(d,parts)
        outputValues.append(val)
        print(val)
    return sum(outputValues)

def main():
    data = parseInput()
    print(part2(data))

if __name__ == "__main__":
    main()
