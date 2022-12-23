with open("Day08\\input.txt", 'r') as f:
    lines = f.read().splitlines()

rowMax = len(lines)-1
colMax = len(lines[0])-1
output = []

def checkCell(r,c, high):
    cell = int(lines[r][c])
    if cell > high:
        output.append(str(r) + '|' + str(c))
        high = cell
    return(high)

## Loop through in the four different directions
#         
for r in range(0, rowMax + 1, 1):
    high = -1
    for c in range(0, colMax + 1, 1):    
        if c == 0:
            high = -1
        high = checkCell(r, c, high)
    for c in range(colMax, -1, -1):  
        if c == colMax:
            high = -1
        high = checkCell(r,c, high)

for c in range(0, colMax + 1):
    print(c)
    high = -1
    for r in range(0, rowMax + 1, 1):
        if r == 0:
            high = -1
        high = checkCell(r, c, high)
    for r in range(rowMax, -1, -1):   
        if r == rowMax:
            high = -1
        high = checkCell(r,c, high)

output = list(dict.fromkeys(output))
print(len(output))




        