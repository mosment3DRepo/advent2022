games = open("Day02\\input.txt", "r").read().split("\n")
score = 0


for i in games:
    if i == '':
        continue
    split = i.split(" ")
    them = ord(split[0])-64
    me = ord(split[1])-87
    if them == me:
        score += 3 + me
        continue
    if them - me == -1 or them - me == 2:
        score += 6 + me
        continue
    else:
        score += me
print(score)

# Part One



# 1 = rock
# 2 = paper
# 3 = scissors

# win = [2, -1, -2][-1,-1,2]
# lose = [-2, 1, 1]
