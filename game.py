import random
def getStrengthOfWarriors():
    strengthWarriorI = random.randint(4,7)
    strengthWarriorII = random.randint(4,7)
    strengthWarriorIII = random.randint(4,7)
    strengthWarriorIV = random.randint(4,7)
    strengthWarriorV = random.randint(4,7)
    strengthWarriorVI = random.randint(4,7)

    strengthOfTeamOne = strengthWarriorI + strengthWarriorII + strengthWarriorIII
    strengthOfTeamTwo = strengthWarriorIV + strengthWarriorV + strengthWarriorVI

    return strengthOfTeamOne, strengthOfTeamTwo

def battleBetTwoTeam(strengthOfTeamOne, strengthOfTeamTwo):
    res = strengthOfTeamOne - strengthOfTeamTwo
    if res > 0:
        winner = 1
        score = res
        return winner, score
    elif res < 0:
        winner = 2
        score = 0-res
        return winner, score
