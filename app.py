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


def mainMenu():
    while True:
        answer = input("Choose the format:\n"
        "1 - Video (mp4)\n"
        "2 - Audio (mp3)\n"
        "3 - Exist\n"
        "Enter the number or type the format (mp4 or mp3):\n")

        if(answer =="1" or answer =="mp4"):
            link = input("Enter the YouTube video URL: ")
            download_video(link)
        elif (answer == "2" or answer =="mp3"):
            link = input("Enter the YouTube video URL: ")
            download_audio(link)
        elif (answer == "exist"):
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    mainMenu()
