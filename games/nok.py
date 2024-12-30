import random as rd
import math

def nok():
    numbers = [rd.randint(1,50) for i in range (3)]
    question = ' '.join(map(str, numbers))
    correct_answer = str(math.lcm(*numbers))
    return question, correct_answer