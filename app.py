# Powerd by José Santos 
# https://github.com/engJoseSantos



# from pytube import YouTube
from pytubefix import YouTube


def Download(link):
    # Create the youtube object
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        # Make the download
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)