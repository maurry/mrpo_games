import sys
sys.path.insert(0, 'C:\\Users\\-\\Desktop\\mrpo_games\\src')
sys.path.insert(0, 'C:\\Users\\-\\Desktop\\mrpo_games\\games')

import nok
import progression

def start_game(chosen_game, player_name):
    for i in range(3):
        match chosen_game:
            case 1:
                question, correct_answer = nok.nok()
                print("Find the smallest common multiple of given numbers.")
                print(f"Question: {question}")
                player_answer = int(input('Your answer: '))
                if player_answer == correct_answer:
                    print('Correct!')
                else:
                    print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
                    print(f"Let's try again, {player_name}!")
            case 2:
                question, correct_answer = progression.progression()
                print("What number is missing in the progression?")
                print(f"Question: {question}")
                player_answer = input('Your answer: ')
                if player_answer == correct_answer:
                    print('Correct!')
                else:
                    print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
                    print(f"Let's try again, {player_name}!")