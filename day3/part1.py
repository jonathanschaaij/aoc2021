file = open("input","r")

numbers = []
for line in file:
    numbers.append(line.strip())

gamma = ""
for x in range(len(numbers[0])):
    total = 0
    for n in numbers:
        if n[x] == "1":
            total += 1
    if total > len(numbers)//2:
        gamma += "1"
    else: 
        gamma += "0"
    
m = 2**len(gamma)-1

g = int(gamma,2)
e = m-g

print(g)
print(e)
print(g*e)
