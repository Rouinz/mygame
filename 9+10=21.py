import random as r
import time
def game():
    global d
    if d < 2:
        print("Welcome to 21 game!")
        d += 1
    time.sleep(1)
    print("Let's get started!")
    choosing = r.randint(0,1)
    count = 0
    rule = [1,2,3]
    while count <= 21:
        if choosing == 0:
            print("Bot turn:")
            bchoice = r.randint(1,3)
            count += bchoice
            time.sleep(1)
            print(bchoice)
            if count >= 21:
                print("You won")
                break
            choosing += 1
        else:
            print("Your turn:")
            pchoice = int(input(""))
            if not(pchoice in rule):
                while not(pchoice in rule):
                    print("Invalid digit, try again")
                    print("Your turn:")
                    pchoice = int(input())
            count += pchoice
            if count >= 21:
                print("Bot won")
                break
            choosing -= 1
    print("Wanna try again?")
    yes_no()
    return
def yes_no():
    y_n = input()
    if y_n == 'y':
        game()
    elif y_n == 'n':
        print("Thanks for playing!")
    else:
        print("I ain't joking, wanna play again or not?")
        while not(y_n == 'y' and y_n == 'n'):
            y_n = input()
            if y_n == 'y':
                game()
            elif y_n == 'n':
                print("Thanks for playing!")
                return
            else:
                k = r.randint(0,2)
                print(speech[k])
d = 1
speech = ["Please stop, yes or no?", "Bro, be serious. Yes or no?", "Are you dumb or something? Yes or no?"]
game()