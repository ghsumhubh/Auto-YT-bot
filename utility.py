import random
from constants import *
import os

def to_uppercase(string):
    tokens = string.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i][0].upper() + tokens[i][1:]
    return " ".join(tokens)

def generate_random_title():
    # pick a random adjective
    title = random.choice(titles)
    song_name = "『" + random.choice(song_names) + "』"
    # to lower case
    title = title.lower()
    title = title.replace("[song name]", song_name)
    title = to_uppercase(title)

    # return the combination of the two
    return title

def generate_random_description():
    finaL_description = ""
    finaL_description += get_random_paragraph() + "\n\n"
    finaL_description += socials + "\n\n\n"

    hashtags_list = []
    # pick hashtags based on rarity
    for hashtag in hashtags:
        threashold = random.randint(0, 1)
        if threashold <= hashtags[hashtag]:
            hashtags_list.append(hashtag)
    # add the symbol
    for i in range(len(hashtags_list)):
        hashtags_list[i] = "#" + hashtags_list[i]
    # shuffle the hashtags
    random.shuffle(hashtags_list)
    finaL_description += " ".join(hashtags_list)
    return finaL_description

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def get_tags():
    return tags

def continue_confirmation():
    input("Press enter to continue")
    

def get_random_paragraph():
    return random.choice(paragraphs)

def get_socials():
    return socials
