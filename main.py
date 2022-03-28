#Rock,Paper,Scissor Game

import random # import random moudle for random number

userwin = 0   #point purposes
computerWin = 0

option = ["rock","paper","scissor"] # declare an variable for using list
          # 0       1       2
while True :
    usercho = input("Please choose (Rock , Paper, Scissor) or Q to exit: ").lower()

    if usercho == "q" :
        print("you won " + str(userwin) + " times.")
        print("Computer won " + str(computerWin) + " times.")
        print("Goodbye !!")
        quit()

    if usercho not in option: #'not in' declare the looping to loop again if option is not in option being declare
        continue

    random_number = random.randint(0,2) #random number for refering the option list

    computerguest = option[random_number]# an variable yang digunakan untuk refering list option dekata atas

    if usercho == "rock" and  computerguest == "scissor": # 'and' to do differetiation between 2 side process
        print("You won !")
        userwin += 1 #Point purposes
        print("Your Point: " ,userwin , "Computer Point: " , computerWin) #Point purposed display
        continue #for repeating the process
    if usercho == "rock" and  computerguest == "rock": #to do differetiation between 2 side process
        print("You deuce !")
        userwin += 0
        print("Your Point: ", userwin, "Computer Point: ", computerWin)
        continue

    if usercho == "paper" and computerguest == "rock":
        print("You won !")
        userwin += 1
        print("Your Point: " ,userwin , "Computer Point: " , computerWin)
        continue
    if usercho == "paper" and computerguest == "paper":
        print("You deuce !")
        userwin += 0
        print("Your Point: " ,userwin , "Computer Point: " , computerWin)
        continue

    if usercho == "scissor" and computerguest == "paper":
        print("You won !")
        userwin += 1
        print("Your Point: " ,userwin , "Computer Point: " , computerWin)
        continue
    if usercho == "scissor" and computerguest == "scissor":
        print("You Deuce !")
        userwin += 0
        print("Your Point: " ,userwin , "Computer Point: " , computerWin)
        continue
    else:
        print("You lost !!"+"The computer choices is "+ computerguest )
        computerWin += 1
        print("Your Point: " ,userwin , "Computer Point: " , computerWin)
        continue














