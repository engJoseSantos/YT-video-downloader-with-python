# YT-video-downloader-with-python

A simple command-line interface tool written in Python to download YouTube videos in MP4 format or convert them directly to MP3.

Features

Video Download: Downloads the highest resolution version of the video as an MP4 file.
Audio Download: Downloads the video's audio track and automatically converts it to MP3, cleaning up the original temporary (MP4) file.
Interactive Menu: Simple terminal interface to select the download format.

Required Libraries

This project requires three Python libraries: pytubefix, moviepy, and pydub (which is a dependency of moviepy).

Use pip to install the dependencies:

pip install pytubefix moviepy


💡 How to Use

Execute the script from your terminal:

python your_script_name.py


(Replace your_script_name.py with the actual name of your Python file).

An interactive menu will be displayed:

Choose the format:
1 - Video (mp4)
2 - Audio (mp3)
3 - Exist
Enter the number or type the format (mp4 or mp3):


(Note: The 'Exist' option in the code should be 'Exit', but the menu is displayed as it is in your current code.)

Select an option:

Type 1 or mp4 to download the video.

Type 2 or mp3 to download and convert to audio.

Type 3 or exist to quit.

The script will then prompt you to Enter the YouTube video URL.

The file will be downloaded to the same directory where the script is being executed.

💻 Code Structure

Function

Description

sanitize_filename(name)

Removes invalid characters from a string to ensure a safe file name.

download_video(link)

Downloads the video at the highest resolution and saves it as MP4.

download_audio(link)

Downloads the audio track as a temporary MP4, uses moviepy to convert it to MP3, and then deletes the temporary MP4 file.

mainMenu()

The main program loop that presents the menu and handles user choices.

📝 Next Steps (TO-DO)

[ ] Replace file name sanitization with a more robust regular expression (regex).

[ ] Add more detailed error handling (e.g., for invalid URLs, network issues).

[ ] Allow the user to choose the download directory.
