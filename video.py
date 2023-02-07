import moviepy.editor as mp
import random
import log
import os
import numpy as np
import cv2
from pydub import AudioSegment
import subprocess

TEMP_AUDIO_PATH="temp_audio.ogg"
TEMP_AUDIO_PATH_EDITED = "temp_audio_edited.ogg"
TEMP_AUDIO_LOOPS_PATH = "temp_before_loops.ogg"
TEMP_IMAGE_PATH = "temp_image.jpg"

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
    final_audio.export(destination, format="ogg")
    del final_audio

def edit_audio(audio_paths, loops=1, compilation=False):
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
    final_audio.export(TEMP_AUDIO_PATH, format="ogg")
    del final_audio
    print("1/6 added pydub edits")

    # sox editing
    one_sox_edit(f"sox {TEMP_AUDIO_PATH} {TEMP_AUDIO_PATH_EDITED} chorus 0.5 0.9 70 0.4 0.25 2 -t 80 0.32 0.4 2.3 -t 60 0.3 0.3 1.3 -s", 2,6)
    one_sox_edit(f"sox {TEMP_AUDIO_PATH} {TEMP_AUDIO_PATH_EDITED} gain -2 pad 0 3 reverb 1.0 0.5 2.0 1.0 0 0",3,6)
    one_sox_edit(f"sox {TEMP_AUDIO_PATH} {TEMP_AUDIO_PATH_EDITED} tempo 0.9",4,6)
    one_sox_edit(f"sox {TEMP_AUDIO_PATH} {TEMP_AUDIO_PATH_EDITED} norm -2.0 equalizer 28 0.91q +6.7 equalizer 4585 1.17q -9.4 equalizer 5356 3.33q +8.4 equalizer 6627 1.58q +7.5 equalizer 11297 1.62q +6.2",5,6)


    # loops
    add_loops(TEMP_AUDIO_PATH, TEMP_AUDIO_LOOPS_PATH, loops)
    print("6/6 added loops (if any)")
    return mp.AudioFileClip(TEMP_AUDIO_LOOPS_PATH)


def edit_picture(picture_path, color_loss=3):
    img = cv2.imread(picture_path)

    # Convert the image from BGR to HSL
    img_hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    # Split the HSL image into channels
    h, l, s = cv2.split(img_hsl)

    # Reduce the saturation channel
    s = (s / color_loss).astype(np.uint8)

    # Merge the channels back into an HSL image
    img_hsl = cv2.merge((h, l, s))

    # Convert the HSL image back to BGR
    img_bgr = cv2.cvtColor(img_hsl, cv2.COLOR_HLS2BGR)

    # Add noise
    noise = np.random.randint(0, 10, img_bgr.shape[:2], np.uint8)
    # same but 3 channels
    noise = np.repeat(noise[:, :, np.newaxis], 3, axis=2)
    blended = cv2.add(img_bgr, noise)
    cv2.imwrite(TEMP_IMAGE_PATH, blended)

    img =  mp.ImageClip(TEMP_IMAGE_PATH)

    # Crop the image to a 16:9 aspect ratio if needed
    cropped_image = img.crop(x1=0, y1=0, x2=img.w, y2=int(img.w*9/16))

    # Resize the image to the desired resolution
    img = cropped_image.resize(width=1920, height=1080)

    return img

def remove_temp_files():
    if os.path.exists(TEMP_AUDIO_PATH):
        os.remove(TEMP_AUDIO_PATH)
    if os.path.exists(TEMP_AUDIO_PATH_EDITED):
        os.remove(TEMP_AUDIO_PATH_EDITED)
    if os.path.exists(TEMP_AUDIO_LOOPS_PATH):
        os.remove(TEMP_AUDIO_LOOPS_PATH)

def make_final_clip(clip, audio):
    final_clip = clip.set_audio(audio.set_duration(clip.duration).audio_fadein(2))
    final_clip = final_clip.set_fps(1)
    final_clip = final_clip.set_duration(audio.duration)
    return final_clip

def save_clip(final_clip, subfolder, filename):
    # check if subfolder "output" exists
    if not os.path.exists("output"):
        os.mkdir("output")
    # check if subfolder exists
    if subfolder:
        if not os.path.exists(f"output/{subfolder}"):
            os.mkdir(f"output/{subfolder}")
        final_clip.write_videofile(f"output/{subfolder}/{filename}")
    else:
        final_clip.write_videofile(f"output/{filename}")


def log_and_cleanup(audio_paths, image_path, remove):
    remove_temp_files()

    #log.log_image(image_file)
    for audio_path in audio_paths:
        log.log_audio(audio_path)
    if remove:
        #os.remove(image_file)
        for audio_path in audio_paths:
            os.remove(audio_path)


def get_image_path():
    image_files = os.listdir("resources/images")
    image_file = random.choice(image_files)
    while log.image_exists(image_file):
        image_file = random.choice(image_files)
    return "resources/images/" + image_file

def get_audio_path():
    audio_files = os.listdir("resources/audio")
    audio_file = random.choice(audio_files)
    while log.audio_exists(audio_file):
        audio_file = random.choice(audio_files)
    return "resources/audio/" + audio_file

def make_video(video_name = "video.mp4", subfolder = None, remove = False):

    image_path = get_image_path()
    audio_paths = [get_audio_path()]
    
    # edit the image in openCV and return a moviepy image
    clip = edit_picture(image_path, color_loss=2)
    audio = edit_audio(audio_paths, loops=1, compilation=False)
    final_clip = make_final_clip(clip, audio)
    save_clip(final_clip, subfolder, video_name)
    log_and_cleanup(audio_paths, image_path, remove)

def make_compilation(video_name = "video.mp4", subfolder = None, remove = False, music_count = 10, loops = 1):

    image_path = get_image_path()
    audio_paths = [get_audio_path() for i in range(music_count)]
    
    # edit the image in openCV and return a moviepy image
    clip = edit_picture(image_path, color_loss=2)
    audio = edit_audio(audio_paths, loops=loops, compilation=True)
    final_clip = make_final_clip(clip, audio)
    save_clip(final_clip, subfolder, video_name)
    log_and_cleanup(audio_paths, image_path, remove)











