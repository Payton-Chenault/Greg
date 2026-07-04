import os
import random

def get_random_picture_path() -> str:
    choice: str = random.choice(os.listdir("assets/pictures"))
    return f"assets/pictures/{choice}"
def get_random_sound_path() -> str:
    choice: str = random.choice(os.listdir("assets/sounds"))
    return f"assets/sounds/{choice}"