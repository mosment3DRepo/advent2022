# For each elf total the calories
# if it's higher than the current variable then add that one

f = open("Day01\\input.txt", "r")
input = f.read()

elves = input.split("\n\n")

bigCal = 0
currentCal = 0

for elf in elves:
    fruitList = elf.split("\n")
    for fruit in fruitList:
        currentCal = currentCal + float(fruit or 0)
        if currentCal > bigCal:
            bigCal = currentCal
    currentCal = 0

print(bigCal)
        


