# Author: Oladapo Okikiola

print("# How to download online videos(e.g. youtube videos) through python\nLearn below👇👇")

print("# first install the pytube module using:\npip install pytube")

import pytube  # importing the pytube module, this a module used to download online videos

video_url = input("Enter url of the video to be downloaded: ")  # asking the user to enter the url of the video to be downloaded

yt = pytube.YouTube(video_url)  # telling the interpreter (which type of video to be downloaded) or (which type of video does the url belongs to)(but in this case it is a youtube video)

for i, stream in enumerate(yt.streams):
    print(f"{i}: {stream.resolution}")

resolution = int(input("Enter the number of resolution you want to be downloaded: "))

video = yt.streams[resolution]

video.download("/storage/emulated/0/Download/")

print("Video has been download, please check your Download folder\n\t'Goodbye'\n\tHope to see you next time")
