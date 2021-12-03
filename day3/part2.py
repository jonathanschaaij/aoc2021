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
eps = bin(e)[2:]

print(g)
print(e)
print(g*e)

O2 = list(set(numbers))
CO2 = list(set(numbers))
x=0
while len(O2) > 1:
    print(O2)
    total = 0
    newArr = []
    for n in O2:
        if n[x] == "1":
            total += 1
    
    mostCommon = "0"
    print("Total = ", total)
    if total >= len(O2)/2:
        mostCommon = "1"
    
    for i, n in enumerate(O2):
        if n[x] == mostCommon:
            newArr.append(n)

    O2 = newArr
    x += 1
    print(x)
print(O2[0])


print("CO2:")
x=0
while len(CO2) > 1:
    print(CO2)
    total = 0
    newArr = []
    for n in CO2:
        if n[x] == "1":
            total += 1
    
    mostCommon = "0"
    if total >= len(CO2)/2:
        mostCommon = "1"
    
    print(mostCommon)
    for n in CO2:
        if n[x] != mostCommon:
            newArr.append(n)
    CO2 = newArr
    x += 1
print(CO2[0])

o = int(O2[0],2)
c = int(CO2[0],2)
print(o)
print(c)
print(c*o)

