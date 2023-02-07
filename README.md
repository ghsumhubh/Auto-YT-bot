# Auto-YT-bot
 A side project for uploading youtube videos automatically.

## Setup
- Put the python files and the bat files(optional) in the same folder.
- Create a folder named "youtubeuploader" and put the required files there (more info in the dependenceis section)
- Create a folder named "images", and put the images there. ([supported formats from opencv's docs](https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html "supported formats from opencv's docs"))
- Create a folder named "audio", and put the audio files there. (supported formats TBD, right now using mp3)

## Usage
The perferred usage is using the interactive CLI interface, to start it type `python ./main.py `  in the CLI. Windows users may also click the "interactive.bat" file.

During the first upload, the program will prompt the user to select a youtube account in a pop-up web page, this is required for the youtubeuploader package to work.

## Features
1. Create lofi-styled videos
2. Create lofi-styled compilations
3. Create and upload lofi-styled videos/compilations.
4. Generate descriptions / titles / etc for videos.

## Dependencies
### youtubeuploader
In order to run the program, it is necessary to create a "youtubeuploader" folder in the same directory as the scripts.
 the folder will contain the executable as well as the required information, as per instructions here: 
https://github.com/porjo/youtubeuploader

Make sure to follow the full setup, as it requires to create an account on the Google Developers Console.

### CV2
`pip install opencv-python`
### Numpy
`pip install numpy`
### Moviepy
`pip install moviepy`
###Pydub
`pip install pydub`
### Sox
Sox 14.4.2
https://sox.sourceforge.net/
Need to add sox to the PATH system variable.

