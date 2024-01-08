from pyfiglet import Figlet
import random


User_Capital = 0

def depositMoney(n):
    global User_Capital
    User_Capital = User_Capital + n
    return User_Capital

def deductMoney(n):
    global User_Capital
    User_Capital = User_Capital - n
    return User_Capital

def cardGenerator():
    numList = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    typeList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    return f"{random.choice(numList)} of {random.choice(typeList)}"

def cardValue(card):
    val = card.split(" ")

    if val[0] == "Two":
        return 2
    elif val[0] == "Three":
        return 3
    elif val[0] == "Four":
        return 4
    elif val[0] == "Five":
        return 5
    elif val[0] == "Six":
        return 6
    elif val[0] == "Seven":
        return 7
    elif val[0] == "Eight":
        return 8
    elif val[0] == "Nine":
        return 9
    elif val[0] == "Ace":
        return 11
    else:
        return 10

def handValue(hand):
    value = 0
    ace = 0
    for i in range(len(hand)):
        if not cardValue(hand[i]) == 11:
            value = value + cardValue(hand[i])
        else:
            ace = ace + 1
    for _ in range(ace):
        if value + 11 <= 21:
            value = value + 11
        else:
            value = value + 1
    return value









def main():
    global User_Capital
    game = True
    round = 0
    game_won = 0
    game_lost = 0
    game_drawn = 0
    wel = True

    while game:

        if wel:
            figlet = Figlet()
            figlet.setFont(font="slant")
            print(figlet.renderText("Welcome to BlackJack Nova"))
            wel = False

        print(f"{'-'*30}\nMENU:\n1. Play\n2. Deposit\n3. Show Balance\n4. Quit\n{'-'*30}")

        while True:
            try:
                choice_Menu = int(input("Pick an option to continue: "))
                if not 0 < choice_Menu < 5:
                    raise ValueError
                else:
                    break

            except ValueError:
                print("ERROR: You must use a number in range 1-4")



        match choice_Menu:
            case 4:
                glo = User_Capital - 1000
                if glo >= 0:
                    print(f"Result:\nYou played {round} games\nYou won: {game_won} round\nYou lost {game_lost} round\nYou draw {game_drawn} round\nYou gained ${glo} amount")
                if glo < 0:
                    print(f"Result:\nYou played {round} games\nYou won: {game_won} round\nYou lost {game_lost} round\nYou draw {game_drawn} round\nYou lost ${-(glo)} amount\nBetter luck next time")

                print("Thank you for playing!")
                game = False
            case 3:
                print("Your Balance is $", User_Capital)
            case 2:
                while True:
                    try:
                        n = int(input("Enter amount in dollars: $ "))
                        if n < 1:
                            raise ValueError
                        depositMoney(n)
                        print("Your Updated Balance is $", User_Capital)
                        break
                    except ValueError:
                        print("ERROR: you must enter a positive number")
            case 1:
                if User_Capital == 0:
                    print("Not enough balance | Please deposit some money")
                    while True:
                        try:
                            n = int(input("Enter amount in dollars: $ "))
                            if n < 1:
                                raise ValueError
                            depositMoney(n)
                            print("Your Updated Balance is $", User_Capital)
                            break
                        except ValueError:
                            print("ERROR: you must enter a positive number")

                round = round + 1
                figlet = Figlet()
                figlet.setFont(font="slant")
                print(figlet.renderText(f"Game Started !\nRound {round}"))


                while True:
                    try:
                        bet = int(input("Please place your bet to play: $ "))
                        if bet >=  User_Capital:
                            raise TypeError
                        if bet <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("ERROR: You have to place a bet bigger than $0")
                    except TypeError:
                        print("ERROR: Your bet is too large compare to your balance! | Please place a smaller bet ")





                match = True
                while match:
                    dealerHand = []
                    playerHand = []
                    for i in range(2):
                        playerHand.append(cardGenerator())
                        dealerHand.append(cardGenerator())
                    print(playerHand)
                    if handValue(playerHand) == 21:
                        print("BLACKJACK!!!")
                        if handValue(dealerHand) == 21:
                            print("Draw")
                            game_drawn = game_drawn + 1
                            match = False
                            print("It is a draw!")
                            input("Press Enter or any key to go back to the Menu: ")
                            break
                        else:
                            print("You won!")
                            game_won = game_won + 1
                            match = False
                            depositMoney(bet)
                            print(f"You won ${bet} amount of money! | Your updated balance is {User_Capital}")
                            input("Press Enter or any key to go back to the Menu: ")
                            break

                    while handValue(dealerHand) < 17:
                        dealerHand.append(cardGenerator())


                    while handValue(playerHand) < 16:
                        print(f"{'-'*30}\nSince your hand is under 16, you have to hit")
                        input("Press Enter or any key to hit: ")
                        playerHand.append(cardGenerator())
                        print(playerHand)
                        if handValue(playerHand) > 21:
                            print("Busted! You lost")
                            game_lost = game_lost + 1
                            match = False
                            deductMoney(bet)
                            print(f"You loss ${bet} amount of money! | Your updated balance is {User_Capital}")
                            input("Press Enter or any key to go back to the Menu: ")
                            break

                    else:
                        cont = True
                        while cont:
                            flag = True
                            while flag:
                                try:
                                    choiceMatch = int(input(f"{'-'*30}\nChoose your action:\n1. Hit\n2. Keep and Reveal\n Your choice: "))
                                    if not 0 < choiceMatch < 3:
                                        raise ValueError
                                    else:
                                        flag = False

                                except ValueError:
                                    print("ERROR: You must use a number in range 1-2")


                            if choiceMatch == 1:
                                playerHand.append(cardGenerator())
                                print(playerHand)
                                if handValue(playerHand) > 21:
                                    print("Busted! You lost")
                                    game_lost = game_lost + 1
                                    cont = False
                                    match = False
                                    deductMoney(bet)
                                    print(f"You loss ${bet} amount of money! | Your updated balance is {User_Capital}")
                                    input("Press Enter or any key to go back to the Menu: ")
                                    break


                            elif choiceMatch == 2:
                                print(f"The dealer hand is:\n{dealerHand}\nThe dealer hand's value is {handValue(dealerHand)}")

                                if handValue(dealerHand) <= 21:
                                    if handValue(playerHand) > handValue(dealerHand):
                                        game_won = game_won + 1
                                        depositMoney(bet)
                                        print(f"You won ${bet} amount of money! | Your updated balance is {User_Capital}")
                                    elif handValue(playerHand) < handValue(dealerHand):
                                        game_lost = game_lost + 1
                                        deductMoney(bet)
                                        print(f"You loss ${bet} amount of money! | Your updated balance is {User_Capital}")
                                    elif handValue(playerHand) == handValue(dealerHand):
                                        game_drawn = game_drawn + 1
                                        print("It is a draw!")
                                elif handValue(dealerHand) > 21 and handValue(playerHand) <= 21:
                                    game_won = game_won + 1
                                    print("The dealer busted!")
                                    depositMoney(bet)
                                    print(f"You won ${bet} amount of money! | Your updated balance is {User_Capital}")

                                input("Press Enter or any key to go back to the Menu: ")
                                cont = False
                                match = False
                                break




if __name__ == "__main__":
    main()



