import os

daynumber = "2"
dataname = f"day{daynumber}.txt"

curdir = os.path.dirname(os.path.abspath(__file__))
filename = f'{curdir}\\{dataname}'
data = [_.strip() for _ in open(filename, 'r').readlines()]

def getVerdictForQ1(opp, mine):
    score = 0
    if(opp == 'A'):
        if(mine == 'Y'):
            #Win
            score += 2
            score += 6
        elif(mine == 'X'):
            #Tie
            #For Rock
            score += 1
            #For tie
            score += 3
        else:
            #Loose with a scissors
            score += 3
    elif (opp == 'B'):
        if(mine == 'Y'):
           
            #Tie
            #For Paper
            score += 2
            #For tie
            score += 3
        elif(mine == 'X'):
           #Loose with a rock
            score += 1
        else:
            #Win with scissors
            score += 3
            score += 6
    #Scissors  
    else:
        if(mine == 'X'):
           
            #Win
            #For Rock
            score += 1
            #For Winning
            score += 6
        elif(mine == 'Y'):
           #Loose with a Paper
            score += 2
        else:
            #Tie with scissors
            score += 3
            score += 3
    return score


def getVerdictForQ2(opp, result):
    score = 0
    #Rock
    if(opp == 'A'):
        if(result == 'X'):
            # Loose
            score += 3
        elif(result == 'Y'):
            # Tie
            # For Rock it should be a rock
            score += 1
            # For tie
            score += 3
        else:
            # Win against a rock
            score += 2
            # For Winning
            score += 6
    elif (opp == 'B'):
        if(result == 'X'):
            # Loose
            score += 1
        elif(result == 'Y'):
            # Tie
            # For Paper it should be a Paper
            score += 2
            # For tie
            score += 3
        else:
            # Win against a paper
            score += 3
            score += 6
    #Scissors  
    else:
        if(result == 'X'):
            # Loose
            score += 2
        elif(result == 'Y'):
            # Tie
            # For Scissors it should be a scissors
            score += 3
            # For tie
            score += 3
        else:
            # Win against a scissors
            score += 1
            score += 6
    return score


totalScore1 = 0
totalScore2 = 0
for line in data:
    words = line.split(' ')
    letter1 = words[0]
    letter2 = words[1]
    totalScore1 += getVerdictForQ1(letter1, letter2)
    totalScore2 += getVerdictForQ2(letter1, letter2)
print(f'First question answer is {totalScore1}\nSecond question answer is {totalScore2}')