import moviepy.editor as mp
import random
import log
import os
import numpy as np
import cv2
from pydub import AudioSegment
import subprocess
from utility import *

TEMP_AUDIO_PATH="temp_audio.flac"
TEMP_AUDIO_PATH_EDITED = "temp_audio_edited.flac"

# TODO: all temp files are created in a temp folder
# TODO: add a progress bar
# TODO: organize the subfolders

def one_sox_edit(command, iteration, max_iterations):
    subprocess.run(command, shell=True, check=True)
    # remove old file and rename new file
    os.remove(TEMP_AUDIO_PATH)
    os.rename(TEMP_AUDIO_PATH_EDITED, TEMP_AUDIO_PATH)
    print(f"{iteration}/{max_iterations} added sox edits")

def add_loops(source, destination, loops):
    # pydub editing
    audio = AudioSegment.from_file(source)
    final_audio = audio * loops
    final_audio.export(destination, format="flac")
    del final_audio

def edit_audio(audio_paths, compilation=False, type="lofi"):
    # pydub editing
    one_second_silence = AudioSegment.silent(duration=1000)
    if compilation:
        audio = one_second_silence
        for i in range(len(audio_paths)):
            audio = audio + AudioSegment.from_file(audio_paths[i])
        audio = audio + one_second_silence
    else: 
        audio = one_second_silence
        audio = audio + AudioSegment.from_file(audio_paths[0])
        audio = audio + one_second_silence
    final_audio = one_second_silence + audio + one_second_silence
    final_audio.export(TEMP_AUDIO_PATH, format="flac")
    del final_audio
    print("1/2 added pydub edits")
    if type == "lofi":
        command = get_sox_lofi_command()
    else:
        #command = get_sox_command()
        pass
    one_sox_edit(f"sox {TEMP_AUDIO_PATH} {TEMP_AUDIO_PATH_EDITED} {command}",2,2)


    return mp.AudioFileClip(TEMP_AUDIO_PATH)

def create_picture_clip(picture_path, has_text = False):
    img = cv2.imread(picture_path)

    # add blur
    img = cv2.GaussianBlur(img, (5,5), 0)
    

    # add text
    if has_text:
        text = "Unleash Your Creativity"
        # needs to support emojis
        font = cv2.FONT_HERSHEY_DUPLEX
        scale = 3
        avg_brightness = np.average(img)
        if avg_brightness > 127:
            color = (255,255,255)
        else:
            color = (0,0,0)
        thickness = 2
        # get text size
        (text_width, text_height) = cv2.getTextSize(text, font, scale, thickness)[0]
        # calculate the position of text
        text_x = img.shape[1] // 2 - text_width // 2
        text_y = img.shape[0] // 2 + text_height // 2

        # add outline
        cv2.putText(img, text, (text_x, text_y), font, scale + 1, color, thickness, cv2.LINE_AA)

    img =  mp.ImageClip(img)
    # Crop the image to a 16:9 aspect ratio if needed and resize it to 1080p
    cropped_image = img.crop(x1=0, y1=0, x2=img.w, y2=int(img.w*9/16))
    img = cropped_image.resize(width=1920, height=1080)

    return img



def remove_temp_files():
    if os.path.exists(TEMP_AUDIO_PATH):
        os.remove(TEMP_AUDIO_PATH)
    if os.path.exists(TEMP_AUDIO_PATH_EDITED):
        os.remove(TEMP_AUDIO_PATH_EDITED)


def add_audio_to_clip(clip, audio, loops=1):
    audio = mp.afx.audio_loop(audio, nloops=loops)
    final_clip = clip.set_audio(audio)
    final_clip = final_clip.set_fps(1)
    final_clip = final_clip.set_duration(audio.duration)
    return final_clip

def save_clip(final_clip, subfolder, video_name):
    # check if subfolder "output" exists
    if not os.path.exists("output"):
        os.mkdir("output")
    # check if subfolder exists
    if subfolder:
        if not os.path.exists(f"output/{subfolder}"):
            os.mkdir(f"output/{subfolder}")
        final_clip.write_videofile(f"output/{subfolder}/{video_name}.mp4")
    else:
        final_clip.write_videofile(f"output/{video_name}.mp4")


def log_and_cleanup(audio_paths, image_path, remove):
    remove_temp_files()

    #log.log_image(image_file)
    for audio_path in audio_paths:
        #log.log_audio(audio_path)
        pass
    if remove:
        #os.remove(image_file)
        for audio_path in audio_paths:
            os.remove(audio_path)


def get_image_path():
    image_files = os.listdir("resources/images")
    image_file = random.choice(image_files)
    #while log.image_exists(image_file):
        #image_file = random.choice(image_files)
    return "resources/images/" + image_file

def get_audio_path():
    audio_files = os.listdir("resources/audio")
    audio_file = random.choice(audio_files)
    #while log.audio_exists(audio_file):
        #audio_file = random.choice(audio_files)
    return "resources/audio/" + audio_file

def make_video(video_name, subfolder = None, remove = False):

    image_path = get_image_path()
    audio_paths = [get_audio_path()]
    
    # edit the image in openCV and return a moviepy image
    clip = create_picture_clip(image_path)
    audio = edit_audio(audio_paths, compilation=False)
    final_clip = add_audio_to_clip(clip, audio, loops=1)
    save_clip(final_clip, subfolder, video_name)
    log_and_cleanup(audio_paths, image_path, remove)

def make_compilation(video_name, subfolder = None, remove = False, music_count = 10, loops = 1):

    image_path = get_image_path()
    audio_paths = [get_audio_path() for i in range(music_count)]
    
    # edit the image in openCV and return a moviepy image
    clip = create_picture_clip(image_path)
    audio = edit_audio(audio_paths, compilation=True)
    final_clip = add_audio_to_clip(clip, audio, loops=loops)
    save_clip(final_clip, subfolder, video_name)
    log_and_cleanup(audio_paths, image_path, remove)











