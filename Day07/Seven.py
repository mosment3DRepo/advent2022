SPACE_TARGET = 30000000

activeDir=[]
fileArray = []
dirTotals = {}
partOne = 0
spaceAvail = 70000000


with open("Day07\\input.txt", 'r') as f:
    commands = f.read().splitlines()
    for c in commands:
        if c[:3] in ('$ l','dir'):
            continue
        if c[:1] == '$':
            if c == '$ cd ..':
                activeDir.pop()
            else:
                activeDir.append(c[5:])
            continue        
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
lowestDelete = 70000000

for item in dirTotals.items():
    if spaceNeeded < item[1] < lowestDelete:
        lowestDelete = item[1]
    if item[1] <= 100000:
        partOne += item[1]

print(partOne)
print(lowestDelete)