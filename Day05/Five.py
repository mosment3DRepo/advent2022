import re
stackUp = []
with open("Day05\\input.txt", 'r') as f:
    lines = f.readlines()
for column in range(9):
    subStack = []
    for row in lines[:8]:
        container = row[(column*4)+1]
        if container != ' ':            
            subStack.append(container)
    stackUp.append(subStack)

for instr in lines[10:]:
    instr = re.split('move | from | to ',instr.strip())
    numMove= int(instr[1])
    numFrom = int(instr[2])-1
    numTo = int(instr[3])-1
    newStack = stackUp[numFrom][:numMove]
    newStack.reverse()
    stackUp[numTo] = newStack + stackUp[numTo]
    del stackUp[numFrom][:numMove]

printOut = ''
for stack in stackUp:
    printOut = printOut + stack[0]
print(printOut)

    
