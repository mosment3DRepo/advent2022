count = 0
with open("Day04\\input.txt", 'r') as f:
    for pairs in f.readlines():
        sPairs = pairs.replace('-',',')
        sPairs = sPairs.strip().split(',')        
        if (int(sPairs[3])-int(sPairs[1]))*(int(sPairs[2])-int(sPairs[0]))<=0:
            count+= 1
print(count)