import sys
sys.path.insert(0, 'C:\\Users\\-\\Desktop\\mrpo_games\\src')
sys.path.insert(0, 'C:\\Users\\-\\Desktop\\mrpo_games\\games')

import cli
import engine

def main():
    name = cli.welcome()
    chosen_game = int(input("What game do you want to play today?\n\
                            1: НОК\n\
                            2: геометрическая прогрессия\n"))

    engine.start_game(chosen_game, name)

if __name__ == "__main__":
    main()

