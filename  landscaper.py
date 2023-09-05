game_data = {
    "money": 0,
    "quit": False
}

## Make $1 cutting lawns using your teeth
def use_teeth():
        user_input = int(input("""
                                What would you like to do?
                                [1] Cut grass using teeth
                                [2] Quit the Game
                                """))
        if (user_input == 1):
            game_data["money"] += 1
            print(f"You cut the grass using teeth and made $1. You have a total of ${game_data['money']}.")
            use_teeth()

        if (user_input == 2):
            game_data["quit"] = True

        if (game_data["quit"] == True):
            print("You quit the game")

use_teeth()
