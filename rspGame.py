import random
userscore = 0
cpuscore = 0
while (True):
    userchoice = int(input("press 1 for rock, 2 for paper and 3 for scissors: "))
    cpuchoice = random.randint(1,3)
    if userchoice == cpuchoice:
        print("Its a tie")
        # rock beats scissor
        # paper beats rock
        # scissor beats paper
    elif userchoice == 1:
        if cpuchoice == 3:
            print("You chose: Rock")
            print("cpu chose scissor. You win")
            userscore +=1
            print("Cpu Score: ",str(cpuscore))
            print("user Score: ",str(userscore))
        if cpuchoice == 2:
            print("You chose: Rock")
            print("cpu chose paper. You lose")
            cpuscore +=1
            print("Cpu Score: ",str(cpuscore))
            print("user Score: ",str(userscore))
    elif userchoice == 2:
        if cpuchoice == 1:
            print("You chose: Paper")
            print("cpu chose Rock. You Win")
            userscore += 1
            print("Cpu Score: ",str(cpuscore))
            print("user Score: ",str(userscore))
        if cpuchoice == 3:
            print("You chose: Paper")
            print("cpu chose scissor. You lose")
            cpuscore +=1
            print("Cpu Score: ",str(cpuscore))
            print("user Score: ",str(userscore))
    elif userchoice == 3:
        if cpuchoice == 2:
            print("You chose: Scissor")
            print("cpu chose Paper. You Win")
            userscore +=1
            print("Cpu Score: ",str(cpuscore))
            print("user Score: ",str(userscore))
        if cpuchoice == 1:
            print("You chose: Scissor")
            print("cpu chose rock. You lose")
            cpuscore +=1
            print("Cpu Score: ",str(cpuscore))
            print("user Score: ",str(userscore))
    if userscore == 5:
        print("Congrats!! You WON The Game")
        break
    if cpuscore == 5:
        print("NOOB!! You LOST The Game")
        break