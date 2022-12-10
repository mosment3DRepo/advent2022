lastFour = []
listCount=0

with open("Day06\\input.txt", 'r') as f:
    signal = f.read()
    for idx, x in enumerate(signal):
        if x not in lastFour:            
            if listCount == 3 and len(lastFour) ==3:
                print(idx + 1)
                exit
            else:
                listCount += 1
                lastFour.append(x)     
        else:
            if listCount != 3:
                listCount += 1
            else:
                del lastFour[0]
        print(x)

    
