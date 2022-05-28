n=18

number_of_guesses=1
print("                                                   || The total number of gusses limited 9 ||")

while (number_of_guesses<=9):
    number = int(input("Gusses the number \n"))

    if number<18:
        print("                                            you enter a too lesser number plz input greater number\n ")

    elif number >18:
        print("                                            you enter a too much greater number plz inmput lesser number\n")

    else:
        print("                                              ***CONGRATS***, Yehh You Win,\n")

        print(number_of_guesses, "no. of gusses left\n")
        break
    print(9-number_of_guesses,"no. of gusses left ")
    number_of_guesses = number_of_guesses+1

    if (number_of_guesses>9):
                print("GAME OVER")