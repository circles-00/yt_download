import os
import sys
import subprocess
import platform

# Install dependency packages function
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install pafy package
install('pafy')
import pafy

# Set yt_api_key
api_key = "Add your api key here"
pafy.set_api_key(api_key)

# Handle download location
def down_location(type, playlist_name=""):
    def_loc_line = None
    if type == 1:
        def_loc_line = "\Single songs"
    elif type == 2:
        def_loc_line = "\Playlists"
    elif type == 3:
        def_loc_line = "\Albums"

    print("Use default download location or a custom one? (Just type 1 or 2)")
    print("1. Default location")
    print("2. Custom location")
    location = int(input())
    if location == 1:
        current_os = platform.system()
        if current_os == "Windows":
            if not os.path.exists("C:\Music"):
                os.mkdir("C:\Music")
            if not os.path.exists("C:\Music" + def_loc_line):
                os.mkdir("C:\Music" + def_loc_line)
            os.chdir("C:\Music" + def_loc_line)
        else:
            if not os.path.exists("/home/Music"):
                os.mkdir("/home/Music")
            if not os.path.exists("/home/Music" + def_loc_line):   
                os.mkdir("/home/Music" + def_loc_line)
            os.chdir("/home/Music" + def_loc_line)
        if playlist_name != "":
            if not os.path.exists(playlist_name):
                os.mkdir(playlist_name)
            os.chdir(playlist_name)
    elif location == 2:
        custom_dir = input("Enter absolute path of custom directory \n")
        os.chdir(custom_dir)
    else:
        print("Invalid input")

def down_playlist(down_type):
    url = input("Enter playlist url: \n")
    playlist = pafy.get_playlist2(url)
    down_location(down_type, playlist.title)

    curr_song = 1
    for song in playlist:
        try:
            print(
                f"Currently downloading song {curr_song}/{len(playlist) + 1} - [{int((curr_song / len(playlist)) * 100)} %]")
            song_video = pafy.new(song.watchv_url)
            audiostreams = song_video.audiostreams
            audiostreams[2].download(song_video.title + ".m4a")
            curr_song += 1
        except:
            pass


if __name__ == '__main__':

    # Main
    print("Choose what type of download you're going to use: (Just type 1, 2 or 3)")
    print("1. A single song")
    print("2. A playlist")
    print("3. An album")
    down_type = int(input())

    if down_type == 1:
        url = input("Enter video url: \n")
        video = pafy.new(url)
        down_location(down_type)
        audiostreams = video.audiostreams
        audiostreams[2].download(video.title + ".m4a")

    elif down_type == 2:
        down_playlist(down_type)

    elif down_type == 3:
        down_playlist(down_type)

    else:
        print("Invalid input")
