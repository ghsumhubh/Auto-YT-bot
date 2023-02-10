

paragraphs = []
# read file located in /resources/paragraphs.txt
with open("resources/text/paragraphs.txt", "r", encoding="utf-8") as f:
    paragraph =""
    for line in f:
        if "#" in line:
            paragraphs.append(paragraph)
            paragraph = ""
        else:
            paragraph += line


# read file located in /resources/socials.txt
with open("resources/text/socials.txt", "r", encoding="utf-8") as f:
    socials = f.read()

# read file located in /resources/song names.txt
with open("resources/text/song names.txt", "r", encoding="utf-8") as f:
    song_names = f.read().split("\n")

# read file located in /resources/titles.txt
with open("resources/text/titles.txt", "r", encoding="utf-8") as f:
    titles = f.read().split("\n")

# read file located in /resources/tags.txt
with open("resources/text/tags.txt", "r", encoding="utf-8") as f:
    tags = f.read().split("\n")

# read file located in /resources/hashtags.txt each line is item:rarity
hashtags = {}
with open("resources/text/hashtags.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.split(":")
        hashtags[line[0]] = float(line[1])
    