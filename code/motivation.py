import random

def Motivation_quete(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            motivation = file.readlines()
        
        # Randomly select a line number between 0 and 69 (assuming 70 lines)
        random_line_number = random.randint(0, min(69, len(motivation) - 1))

        # Get the motivation from the randomly chosen line
        random_motivation = motivation[random_line_number].strip()

        return random_motivation
    except Exception as e:
        print(f"Error reading motivation file: {e}")
        return "Sorry, I couldn't fetch a motivation quote at the moment."
