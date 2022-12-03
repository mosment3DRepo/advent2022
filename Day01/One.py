elves = open("Day01\\input.txt", "r").read().split("\n\n")
bigCal = [0,0,0]
currentCal = 0
for elf in elves:
    fruitList = elf.split("\n")
    for fruit in fruitList:
        currentCal = currentCal + float(fruit or 0)
        if currentCal > bigCal[0]:
            bigCal[0] = currentCal
            bigCal.sort()
    currentCal = 0
print(bigCal[2])
print(sum(bigCal))
        


