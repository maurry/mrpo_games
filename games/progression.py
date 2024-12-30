import random

def progression():
    starting_number = random.randint(1, 10)
    common_ratio = random.randint(2, 10)
    sequence_length = random.randint(5, 8)

    sequence = [starting_number*common_ratio**t for t in range(sequence_length)]
    
    hidden_index = random.randint(0, sequence_length - 1)
    correct_answer = str(sequence[hidden_index])
    sequence[hidden_index] = ".."
    question = " ".join(map(str, sequence))
    return question, correct_answer



