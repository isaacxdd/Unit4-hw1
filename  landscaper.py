game_data = {
    "money": 0,
    "quit": False
}

## Make $1 cutting lawns using your teeth
def use_teeth():
    while(True):
        user_input = int(input("""
                                What would you like to do?
                                [1] Cut grass using teeth
                                [2] Quit the Game
                                """))
        if (user_input == 1):
            game_data["money"] += 1
            print(f"You cut the grass using teeth and made $1. You have a total of ${game_data['money']}.")
           if game_data["money"] >= 5:
                buy_rusty_scissors()

       else if (user_input == 2):
            game_data["quit"] = True
            print("You quit the game")
else:
            print("Invalid input. Please choose a valid option.")

def buy_rusty_scissors()
    while(True):
        user_input = int(input(""" 
                        Would you like to buy a pair of rusty scissors for $5?
                        [1] Yes, my teeth could use a break
                        [2] No
                        [3] Quit the Game
                        """))
     if(user_input == 1):

            game_data["money"] -= 5

            print(f"You have purchased a pair of rusty scissors for $5 and now have ${game_data['money']}.")

            use_rusty_scissors()

        if(user_input == 2):

            game_data["money"] +=1

            use_teeth()

        else if (user_input == 2):

            game_data["quit"] = True   
            print("You quit the game")

             else:
            print("Invalid input. Please choose a valid option.")




def use_rusty_scissors():

    while(True):

        user_input = int(input("""

                            Would you like to use your rusty scissors to cut grass for $5?

                            [1] Yes

                            [2] No, I want to go back to using my teeth

                            [3] Quit the Game

                            """))

        if(user_input == 1):

            game_data["money"] += 5

            print(f"You cut the grass using rusty scissors and made $5. You have a total of ${game_data['money']}.")

        if game_data["money"] >= 25:
                buy_push_lawnmower()


        else if(user_input == 2):

            game_data["money"] += 1

            print(f"You cut the grass using teeth and made $1. You have a total of ${game_data['money']}.")

            use_teeth()

        elif (user_input == 3):
            game_data["quit"] = True
            print("You quit the game")

        else:
            print("Invalid input. Please choose a valid option.")


def buy_push_lawnmower():
    while(True):
        user_input = int(input(""" 
                        Would you like to buy a push lawnmower for $25?
                        [1] Yes
                        [2] No
                        [3] Quit the Game
                        """))

        if(user_input == 1):
            game_data["money"] -= 25
            print(f"You have purchased a push lawnmower for $25 and now have ${game_data['money']}.")
            use_push_lawnmower()

        elif(user_input == 2):
            game_data["money"] += 5
            use_rusty_scissors()

        elif (user_input == 3):
            game_data["quit"] = True
            print("You quit the game")

        else:
            print("Invalid input. Please choose a valid option.")


def use_push_lawnmower():
    while(True):
        user_input = int(input("""
                            Would you like to use your push lawnmower to mow the lawn for $50?
                            [1] Yes
                            [2] No, I want to use my rusty scissors
                            [3] Quit the Game
                            """))
        if(user_input == 1):
            game_data['money'] += 50
            print(f"You mowed the lawn using the push lawnmower and earned $50. You now have ${game_data['money']}.")
            if game_data["money"] >= 250:
                buy_battery_powered_lawnmower()

        elif(user_input == 2):
            game_data['money'] +=5
            print(f"You cut the grass using rusty scissors and made $5. You have a total of ${game_data['money']}.")

        elif(user_input == 3):
            game_data["quit"] = True
            print("You quit the game")

        else:
            print("Invalid input. Please choose a valid option.")
       
            break
use_teeth()