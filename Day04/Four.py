count = 0
count2 = 0


with open("Day04\\input.txt", 'r') as f:
    for pairs in f.readlines():
        sPairs = pairs.replace('-',',')
        sPairs = sPairs.strip().split(',')         
        sPairsInt = list(map(int, sPairs))
        f = sPairsInt.index(min(sPairsInt))   
        if (sPairsInt[3]-sPairsInt[1])*(sPairsInt[2]-sPairsInt[0])<=0:
            if sPairsInt[f+1] >= sPairsInt[abs(f-3)] or sPairsInt[f] == sPairsInt[abs(f-2)]:
                count += 1
        if sPairsInt[f+1] >= sPairsInt[abs(f-2)]:
            count2 += 1

        
print(count)
print(count2)