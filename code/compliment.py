import random

def get_random_compliment_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        compliments = file.readlines()
    # Randomly select a line number between 0 and 99 (assuming 100 lines)
    random_line_number = random.randint(0, min(99, len(compliments) - 1))

    # Get the compliment from the randomly chosen line
    random_compliment = compliments[random_line_number].strip()

    return random_compliment
