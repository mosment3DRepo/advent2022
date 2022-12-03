elves = open("Day01\\input.txt", "r").read().split("\n\n")
bigCal = []
currentCal = 0
for elf in elves:
    fruitList = elf.split("\n")
    for fruit in fruitList:
        currentCal += float(fruit or 0)
    bigCal.append(currentCal)
    currentCal = 0
bigCal.sort(reverse=True)
print(bigCal[0])
print(sum(bigCal[:2]))
        


