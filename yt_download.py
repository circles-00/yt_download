import os
import sys
import subprocess
import platform


# Install dependency packages function
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Install pafy package
install('pafy')
install('youtube-dl')
import pafy

# Set yt_api_key
api_key = "Add your api key here"
pafy.set_api_key(api_key)


# Handle download location
def down_location(type, playlist_name="", artist=""):
    def_path = None
    current_os = platform.system()
    if current_os == "Windows":
        def_path = "C:\Music\\"
    else:
        def_path = "/home/Music/"

    if type == 1:
        def_path += "Single songs"
    elif type == 2:
        def_path += "Playlists"
    elif type == 3:
        def_path += "Albums"

    print("Use default download location or a custom one? (Just type 1 or 2)")
    print("1. Default location")
    print("2. Custom location")
    location = int(input())
    if location == 1:
        if not os.path.exists(def_path):
            os.makedirs(def_path)
        os.chdir(def_path)

        if artist != "":
            if not os.path.exists(artist):
                os.mkdir(artist)
            os.chdir(artist)
            
        if playlist_name != "":
            if not os.path.exists(playlist_name):
                os.mkdir(playlist_name)
            os.chdir(playlist_name)

    elif location == 2:
        custom_dir = input("Enter absolute path of custom directory \n")
        os.chdir(custom_dir)
    else:
        print("Invalid input")


def down_playlist(down_type, artist=""):
    url = input("Enter playlist url: \n")
    playlist = pafy.get_playlist2(url)
    down_location(down_type, playlist.title, artist)

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
            continue


if __name__ == '__main__':

    # Main
    while True:
        down_type, url = None, None
        print("Choose what type of download you're going to use: (Just type 1, 2 or 3)")
        print("1. A single song")
        print("2. A playlist")
        print("3. An album")
        try:
            down_type = int(input())
        except:
            pass

        if down_type == 1:
            try:
                url = input("Enter video url: \n")
                video = pafy.new(url)
            except:
                print("Invalid url")
                continue

            down_location(down_type)
            audiostreams = video.audiostreams
            audiostreams[2].download(video.title + ".m4a")

        elif down_type == 2:
            down_playlist(down_type)

        elif down_type == 3:
            artist = input("Enter artist name: \n")
            down_playlist(down_type, artist)

        else:
            print("Invalid input")

        print("Script has finished executing")
        con = input("Do you wish to continue downloading?[y\\n]\n")
        if con == 'y':
            continue
        else:
            break
