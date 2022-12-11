lastFour = []

with open("Day06\\input.txt", 'r') as f:
    signal = f.read()
    for ind, x in enumerate(signal):
        try:
            del lastFour[:lastFour.index(x)+1]
        except:
            if len(lastFour) == 3:
                print('done! '+ str(ind+1)+ ' ' + str(lastFour + [x]))
                break
        lastFour.append(x) 

    
