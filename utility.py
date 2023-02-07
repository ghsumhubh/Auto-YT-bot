import random
from constants import adjectives, nouns, sentences, tags
import os

def to_uppercase(string):
    tokens = string.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i][0].upper() + tokens[i][1:]
    return " ".join(tokens)

def generate_random_title():
    # pick a random adjective
    first_word = "Lofi Study Music"
    opening_bracket = "『"
    closing_bracket = "』"
    adjective = to_uppercase(random.choice(adjectives))
    noun = to_uppercase(random.choice(nouns)) 
    words = [first_word, opening_bracket, adjective, noun, closing_bracket]

    # return the combination of the two
    return first_word + opening_bracket + adjective + " " + noun + closing_bracket

def generate_random_description():
    # pick a random sentence
    sentence = random.choice(sentences)
    # pick 4-8 random tags
    line_drops = "\n\n\n\n\n"
    random_tags = random.sample(tags, random.randint(4, 8))
    # return the combination of the two
    return sentence + line_drops + "tags: " +", ".join(random_tags) + "."

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def continue_confirmation():
    input("Press enter to continue")