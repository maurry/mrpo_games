import sys


import src.cli
import src.engine

def main():
    name = src.cli.welcome()
    chosen_game = int(input("What game do you want to play today?\n\
                            1: НОК\n\
                            2: геометрическая прогрессия\n"))

    src.engine.start_game(chosen_game, name)

if __name__ == "__main__":
    main()

