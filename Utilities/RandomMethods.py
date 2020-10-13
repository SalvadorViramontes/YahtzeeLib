import random
import string

def get_random_name():
    name = random.choice(string.ascii_uppercase)
    return name + ''.join(random.choice(string.ascii_lowercase) for i in range(5))

def randomChoice():
    return random.random() > 0.5