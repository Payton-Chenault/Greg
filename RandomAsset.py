import os
import random

from ResourceUtil import resource_path


def get_random_picture_path() -> str:
    choice: str = random.choice(os.listdir(resource_path("assets/pictures")))
    return f"assets/pictures/{choice}"
def get_random_sound_path() -> str:
    choice: str = random.choice(os.listdir(resource_path("assets/sounds")))
    return f"assets/sounds/{choice}"