count = 0
count2 = 0
with open("Day04\\input.txt", 'r') as f:
    for pairs in f.readlines():
        sPairs = pairs.replace('-',',')
        sPairs = sPairs.strip().split(',')         
        sPairsInt = list(map(lambda a: int(a), sPairs))
        smaller = sPairsInt.index(min(sPairsInt))   
        if (sPairsInt[3]-sPairsInt[1])*(sPairsInt[2]-sPairsInt[0])<=0:
            count += 1
        if sPairsInt[smaller+1] >= sPairsInt[abs(smaller-2)]:
            count2 += 1

        
print(count)
print(count2)