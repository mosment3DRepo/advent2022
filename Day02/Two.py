# Not particularly elegant, should use a function next time

games = open("Day02\\input.txt", "r").read().split("\n")
score = 0
scoreTwo = 0


for i in games:
    if i == '':
        continue
    split = i.split(" ")
    them = ord(split[0])-64
    me = ord(split[1])-87
    # answer 1
    if them == me:
        score += 3 + me
        continue
    if them - me == -1 or them - me == 2:
        score += 6 + me
        continue
    else:
        score += me

for i in games:
    if i == '':
        continue
    split = i.split(" ")
    them = ord(split[0])-64
    me = ord(split[1])-87
    # answer 1
    if me == 2:
        scoreTwo += 3 + them
        continue
    if me == 1:
        if them - 1 == 0:
            scoreTwo += 3
        else:
            scoreTwo += them - 1
        continue
    else:
        if them + 1 == 4:
            scoreTwo += 6 + 1
        else:
            scoreTwo += 6 + them + 1
        continue
        

print(score)
print(scoreTwo)


# 1 = rock
# 2 = paper
# 3 = scissors

# win = [2, -1, -2][-1,-1,2]
# lose = [-2, 1, 1]
