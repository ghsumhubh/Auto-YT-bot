from utility import clear_screen, continue_confirmation
from routines import *
import sys

def interactive_upload():
    clear_screen()
    print ("1. Upload videos")
    print ("2. Upload videos with compilation")
    print ("3. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        video_amount = input("Enter video amount: ")
        success_count = normal_routine(int(video_amount))
        answer =  "Uploaded {} videos".format(success_count)
        if success_count != int(video_amount):
            answer += " ({} failed)".format(int(video_amount) - success_count)
        return answer
    elif choice == "2":
        video_amount = input("Enter video amount: ")
        music_count = input("Enter music count: ")
        loops = input("Enter loops: ")
        success_count = normal_routine_compilation(int(video_amount), int(music_count), int(loops))
        answer =  "Uploaded {} videos with compilation".format(success_count)
        if success_count != int(video_amount):
            answer += " ({} failed)".format(int(video_amount) - success_count)
        return answer
    elif choice == "3":
        return

def interactive_create():
    clear_screen()
    print ("1. Create videos")
    print ("2. Create videos with compilation")
    print ("3. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        video_amount = input("Enter video amount: ")
        subfolder = input("Enter subfolder name: ")
        clear_screen()
        create_only_routine(int(video_amount), subfolder)
        return "Created {} videos in subfolder {}".format(video_amount, subfolder)
    elif choice == "2":
        video_amount = input("Enter video amount: ")
        subfolder = input("Enter subfolder name: ")
        music_count = input("Enter music count: ")
        loops = input("Enter loops: ")
        clear_screen()
        create_only_routine_compilation(int(video_amount), subfolder, int(music_count), int(loops))
        return "Created {} videos with compilation in subfolder {}".format(video_amount, subfolder)
    elif choice == "3":
        return

def interactive_generate():
    clear_screen()
    print ("1. Generate video names")
    print ("2. Generate video descriptions")
    print ("3. Generate video tags")
    print ("4. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        video_amount = input("Enter video amount: ")
        clear_screen()
        names_only_routine(int(video_amount))
        continue_confirmation()
        return "Generated {} video names".format(video_amount)
    elif choice == "2":
        video_amount = input("Enter video amount: ")
        clear_screen()
        descriptions_only_routine(int(video_amount))
        continue_confirmation()
        return "Generated {} video descriptions".format(video_amount)
    elif choice == "3":
        clear_screen()
        tags_only_routine()
        continue_confirmation()
        return "Generated video tags"
    elif choice == "4":
        return

def show_main_menu(result):
    clear_screen()
    if result:
            print("====================================")
            print(result)
            print("====================================")
            print("\n")
    print("What do you want to do?")
    print("1. Upload videos")
    print("2. Create videos")
    print("3. Generate content descriptions")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def interactive_interface():
    result = ""
    while True:
        choice = show_main_menu(result)
        if choice == "1":
            result = interactive_upload()
        elif choice == "2":
            result = interactive_create()
        elif choice == "3":
            result = interactive_generate()
        elif choice == "4":
            sys.exit(0)

def old_argument_interface(args):
    command = args[1]
    if command == "upload":
        try:
            video_amount = int(args[2])
            normal_routine(video_amount)
        except:
            print("invalid video amount")
    
    elif command == "upload_compilation":
        try:
            video_amount = int(args[2])
            normal_routine_compilation(video_amount)
        except:
            print("invalid video amount")
    elif command == "create":
        try:
            video_amount = int(args[2])
            subfolder = args[3]
            create_only_routine(video_amount, subfolder)
        except:
            print("invalid video amount or subfolder")
    elif command == "create_compilation":
        try:
            video_amount = int(args[2])
            subfolder = args[3]
            create_only_routine_compilation(video_amount, subfolder)
        except:
            print("invalid video amount or subfolder")
    elif command == "names":
        try:
            video_amount = int(args[2])
            names_only_routine(video_amount)
        except:
            print("invalid video amount")
    else:
        print("available commands: upload, upload_compilation, create, create_compilation, names")
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        interactive_interface()
    else:
        old_argument_interface(sys.argv)
     
if __name__ == "__main__":
    main()







        
