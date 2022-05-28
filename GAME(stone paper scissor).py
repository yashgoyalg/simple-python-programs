import random

print("\n\t\t\t\t\t\t\tLet\'s start the game \"STONE PAPER SCISSOR\"")
count = 0
win = 0
draw = 0
lst = ["Stone", "Paper", "scissor"]
print("\n\t\t\t\t\t\t\t(0 for Stone, 1 for Paper, 2- Scissor)")
while count<10:
    Computer = random.randint(0,2)
    print("\t\t\t\t\t\t\t\t***TURN - ", str(count+1), "***")
    user = int(input("\t\t\t\t\t\t\tPlease insert your choice : "))
    while user>2 or user<0:
        print("Your input is not valid")
        user = int(input("Please insert again : "))
        print("Your Choice : ", lst[user])
    print("Computer's Choice : ", lst[Computer])
    if user == Computer:
        print("Draw!")
        draw += 1
    else:
        if user == 0:
            if Computer == 1:
                print("WOW,You lost the Game")
                win += 1
            if Computer == 2:
                print("You win the Game")
        elif user == 1:
            if Computer == 0:
                print("You win the Game")
            if Computer == 2:
                print("You lost the Game")
                win += 1
        elif user == 2:
            if Computer == 0:
                print("You lost the Game")
                win += 1
                if Computer == 1:
                    print("You win the Game")
    count+=1
print("\n\t*****RESULTS*****\t\n")
print("You Win : ", str(win))
print("Computer Win : ", str(10-win-draw))
print("No. of Drawn : ", str(draw))