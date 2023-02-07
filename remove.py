import os
def remove_video(filename):
    os.remove(filename)
    print("Removed video file: {}".format(filename))