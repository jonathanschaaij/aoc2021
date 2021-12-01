file = open("day1.txt","r")

n = 0
count = 0
for i,line in enumerate(file):
    line = line.strip()
    if i == 0:
        n = int(line)
        continue

    a = int(line)
    if a > n:
        count += 1
    n=a
print(count)
