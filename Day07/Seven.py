SPACE_TARGET = 30000000

list = False
activeDir=[]
fileArray = []
dirTotals = {}
partOne = 0
spaceAvail = 70000000
lowestDelete = 70000000

with open("Day07\\input.txt", 'r') as f:
    commands = f.read().splitlines()
    for c in commands:
        if c[:4] == '$ ls':
            list = True
            continue
        if c == '$ cd ..':
            activeDir.pop()
            list = False
            continue
        if c[:4] == '$ cd':
            activeDir.append(c[5:])
            list = False
            continue
        if list == True and c[:3] != 'dir':
            size = int(c.split(' ')[0])
            spaceAvail -= size
            for i in range(len(activeDir)):
                loc = activeDir[:i+1]
                locString = '/'.join(loc)
                try:
                    dirTotals[locString] = dirTotals[locString] + size
                except KeyError:
                    dirTotals[locString] = size

spaceNeeded = SPACE_TARGET - spaceAvail

for item in dirTotals.items():
    if spaceNeeded < item[1] < lowestDelete:
        lowestDelete = item[1]
    if item[1] <= 100000:
        partOne += item[1]

print(partOne)
print(lowestDelete)