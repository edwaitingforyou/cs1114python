import game
def getNameOfTeam():
    print 'Player 1'
    nameOfTeamOne = raw_input("Enter the name of your team:")
    print 'Player 2'
    nameOfTeamTwo = raw_input("Enter the name fo your team:")
    return nameOfTeamOne, nameOfTeamTwo

def displayRes(nameOfTeamOne,nameOfTeamTwo,winner,score):
    print "Both team fought valiantly and"
    if winner == 1:
        print nameOfTeamOne,"emerges victorious!"
        print "(They won by",score,"strength units)"
    elif winner == 2:
        print nameOfTeamTwo,"emerges victorious!"
        print "(They won by",score,"strength units)"



def main():
    strengthOfTeamOne,strengthOfTeamTwo = game.getStrengthOfWarriors()
    winner, score = game.battleBetTwoTeam(strengthOfTeamOne, strengthOfTeamTwo)
    nameOfTeamOne, nameOfTeamTwo = getNameOfTeam()
    displayRes(nameOfTeamOne,nameOfTeamTwo,winner,score)


main()
