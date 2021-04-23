#Lists
laxPositions = ['Midfielder', 'Attacker', 'Defenseman', 'Goalie']

#Variables
middie = 0
attack = 0
defense = 0
goalie = 0

#Inputs
hundredYard = input('How fast is your 100 yard dash? (In seconds): ')
experienceCheck = input('Have you played lacrosse before? (Respond Y/N): ')
otherSports = input("How any other sports do you play (Enter a number)?: ")
glassesCheck = input("Do you wear glasses? (Respond Y/N)?: ")

#Algorithims
    
def positionDeterminer():
    global middie
    global attack
    global defense
    global goalie
    #Speed
    if int(hundredYard) > 15:
        defense += 1
        goalie += 2
    else:
        middie += 1
        attack +=1
    #Lax Experience
    if experienceCheck.lower() == 'y':
        attack += 1
        defense += 1
        goalie += 1
    else:
        middie += 1
        defense += 1
    #Other Sport Experience
    if int(otherSports) == 0:
        middie += 1
        defense += 1
    elif int(otherSports) >= 1:
        attack += 1
        goalie += 1
    #Vision
    if glassesCheck.lower() == 'y':
        goalie -= 1

    userScores = [middie, attack, goalie, defense]

    if max(userScores) == middie:
        print("You should play as a " + laxPositions[0])

    elif max(userScores) == attack:
        print("You should play as an " + laxPositions[1])

    elif max(userScores) == defense:
        print("You should play as a " + laxPositions[2])

    elif max(userScores) == goalie:
        print("You should play as a " + laxPositions[3])


    print(userScores)

positionDeterminer()
