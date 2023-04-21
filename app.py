from game import Game


def start_game():
    game_instance = Game()
    game_instance.welcome()
    while game_instance.get_play_again() == 1:
        game_instance = Game()
        game_instance.start()
    print("\nGAME ENDING...\nGOODBYE\n")


def main():
    start_game()
    # phrase()


if __name__ == '__main__':
    main()
