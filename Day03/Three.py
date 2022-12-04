backpackList= 0
with open("Day03\\input.txt", 'r') as f:
    for backpack in f.readlines():
        containerSize = int(len(backpack)/2)
        container1 = [*backpack[0:containerSize]]
        container2 = [*backpack [containerSize:]]
        a = ''.join(set(container1).intersection(container2))
        if a.isupper():
            backpackList += ord(a)-38
        else:
            backpackList += ord(a)-96
print(backpackList)
    

#     test = ord("G")-64
#     testLow = ord("g")-96