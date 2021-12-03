file = open("day1.txt", "r")

count = 0
n = []
for i, line in enumerate(file):
    line = line.strip()
    n.append(int(line))
    
sums = []
for i in range(0,len(n)-2):
    sums.append(sum(n[i:i+3])) 

for n in range(1,len(sums)):
    if sums[n]>sums[n-1]:
        count +=1
print(count)
