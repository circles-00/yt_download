With this python script you can download youtube videos in m4a format.

You must have python installed to be able to use this script.

Usage: python3 yt_download.py

Features:
1. Download a single song
2. Download a whole playlist
3. Download a whole album

You can either download in:
1. Default location: "C:\Music" for Windows, "/home/Music" for Linux
2. Custom location(You can input custom absolute path)

To be able to start using this script, you have to first edit line 7 with your youtube data api key, you can read more about it here: https://developers.google.com/youtube/v3/getting-started

Note for Linux users: Run the script in root mode, for example sudo python3 yt_download.py

Note: After you use the script for the first time, feel free to comment out lines 13 & 14 for faster execution. This is not a necessary action, you can completely ignore this note if you feel lazy to do it.

Note: If you get HTTP Error 404 or 403 error code, it's nothing to worry about, just re-run the script.
