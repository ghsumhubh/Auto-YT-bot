import subprocess
import os
import json
from utility import generate_random_description, generate_random_title, get_tags


def upload_video(video_name):
    path = f"output/{video_name}.mp4"
    # create a file called "metadata.json"
    create_metadata_file(description=generate_random_description(),video_name=generate_random_title(), tags=get_tags())
    # run a command in terminal to upload the video
    completed_process = subprocess.run(["./youtubeuploader/youtubeuploader", "-filename", video_name, "-metaJSON", "metadata.json"])
    # delete the metadata file
    delete_metadata_file()
    
    if completed_process.returncode != 0:
        print("Quota reached")
        return True

    return False

def delete_metadata_file():
    os.remove("metadata.json")

def create_metadata_file(description, video_name, tags):
    data = {
    "title": video_name,
    "description": description,
    "tags": tags,
    "privacyStatus": "public",
    "madeForKids": False,
    "embeddable": True,
    "license": "creativeCommon",
    "publicStatsViewable": True,
    "categoryId": "10",
    "language":  "en"
    }

    with open("metadata.json", "w") as f:
        json.dump(data, f)




