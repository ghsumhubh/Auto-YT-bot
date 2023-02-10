
from utility import clear_screen
from video import make_video, make_compilation
from upload import upload_video
from remove import remove_video
from utility import clear_screen, generate_random_title, generate_random_description, get_tags

def normal_routine(num_of_videos):
    for i in range(num_of_videos):
        clear_screen()
        print("Working on video {}/{}".format(i+1, num_of_videos))
        video_name = "video-{}.mp4".format(i)
        make_video(video_name, remove=False)
        clear_screen()
        print("Uploading video {}/{}".format(i+1, num_of_videos)) 
        had_error = upload_video(f"output/{video_name}") 
        remove_video(f"output/{video_name}")
        if had_error:
            return i
    return num_of_videos

def normal_routine_compilation(num_of_videos, music_count=10, loops=1):
    for i in range(num_of_videos):
        clear_screen()
        print("Working on video {}/{}\n\n".format(i+1, num_of_videos))
        video_name = "video-{}.mp4".format(i)
        make_compilation(video_name, remove=False, music_count = music_count, loops = loops)
        clear_screen()
        print("Uploading video {}/{}\n\n".format(i+1, num_of_videos))
        had_error = upload_video(f"output/{video_name}") 
        remove_video(f"output/{video_name}")
        if had_error:
            return i
    return num_of_videos

def create_only_routine(num_of_videos, subfolder):
    for i in range(num_of_videos):
        clear_screen()
        print("Working on video {}/{}\n\n".format(i+1, num_of_videos))
        video_name = "video-{}.mp4".format(i)
        make_video(video_name, subfolder, remove=False)

def create_only_routine_compilation(num_of_videos, subfolder, music_count=10, loops=1):
    for i in range(num_of_videos):
        clear_screen()
        print("Working on video {}/{}\n\n".format(i+1, num_of_videos))
        video_name = "video-{}.mp4".format(i)
        make_compilation(video_name, subfolder, remove=False, music_count = music_count, loops = loops)

def names_only_routine(num_of_names):
    clear_screen()
    for i in range(num_of_names):
        print(generate_random_title())

def descriptions_only_routine(num_of_descriptions):
    clear_screen()
    for i in range(num_of_descriptions):
        print(generate_random_description())

def tags_only_routine():
    clear_screen()
    print(get_tags())
