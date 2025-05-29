# Powerd by José Santos 
# https://github.com/engJoseSantos


# from pytube import YouTube # Old library
from pytubefix import YouTube
from moviepy import AudioFileClip
import os


def sanitize_filename(name):
    # TO-CHANGE to regex
    return "".join(c for c in name if c.isalnum() or c in " ._-").strip() 

def download_video(link):
    # Create the youtube object
    youtubeObject = YouTube(link)
    videoStream = youtubeObject.streams.get_highest_resolution()
    try:
        # Make the download
        videoStream.download(filename=sanitize_filename(youtubeObject.title) + ".mp4")
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def download_audio(link):
    # Create the youtube object
    youtubeObject = YouTube(link)
    audioStream = youtubeObject.streams.filter(only_audio=True).first()
    filename = sanitize_filename(youtubeObject.title)
    try:
        # Make the download
        downloaded_file = audioStream.download(filename=sanitize_filename(youtubeObject.title) + ".mp4")
    except:
        print("An error has occurred")
    print("Try to convert")

    try:
        # Converte para mp3
        clip = AudioFileClip(downloaded_file)
        clip.write_audiofile(filename + ".mp3")
        clip.close()
        os.remove(downloaded_file)  # remove the file
    except:
        print("An error has occurred")
    print("Download is completed successfully")




link = input("Enter the YouTube video URL: ")
download_audio(link)
#download_video(link)
