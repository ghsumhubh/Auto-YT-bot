import os

def create_log_file_if_not_exists():
    # check if folder "logs" exists
    if not os.path.exists("logs"):
        os.makedirs("logs")
    # check if file "logs/images.txt" exists
    if not os.path.exists("logs/images.txt"):
        # if not, create it
        with open("logs/images.txt", "w") as f:
            f.write("")
            print("Created log file")
    # check if file "logs/errors.txt" exists
    if not os.path.exists("logs/errors.txt"):
        # if not, create it
        with open("logs/errors.txt", "w") as f:
            f.write("")
            print("Created log file")
    # check if file "logs/audio.txt" exists
    if not os.path.exists("logs/audio.txt"):
        # if not, create it
        with open("logs/audio.txt", "w") as f:
            f.write("")
            print("Created log file")

def log_image(image_file):
    create_log_file_if_not_exists()
    with open("logs/images.txt", "a") as f:
        f.write(image_file)
        f.write("\n")
    
def log_audio(audio_file):
    create_log_file_if_not_exists()
    with open("logs/audio.txt", "a") as f:
        f.write(audio_file)
        f.write("\n")

def log_error(error):
    create_log_file_if_not_exists()
    with open("logs/errors.txt", "a") as f:
        f.write(error)
        f.write("\n")

def image_exists(image_file):
    create_log_file_if_not_exists()
    with open("logs/images.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if image_file in line:
                return True
        return False

def audio_exists(audio_file):
    create_log_file_if_not_exists()
    with open("logs/audio.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if audio_file in line:
                return True
        return False
    
