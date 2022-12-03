# For each elf total the calories
# if it's higher than the current variable then add that one

f = open("input.txt", "r")
input = f.read()

bigCal = 0

for x in input:
    if x == "\n":
        currentCal = 0
    else:
        currentCal = currentCal + x
    if currentCal > bigCal:
        bigCal = currentCal
    else:
        next

    

