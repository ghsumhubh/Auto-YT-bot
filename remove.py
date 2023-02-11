import os
def remove_video(video_name):
    path = f"output/{video_name}.mp4"
    os.remove(path)
    print("Removed video file: {}".format(path))