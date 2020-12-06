# ytdl-bot

Telegram bot for audio downloading. Built on FFmpeg and youtube-dl. Works with most sites, can download YouTube playlists, split large audio files into pieces to overcome Bot api limit.

## Requirements

- ffmpeg
- Python 3

## Installing

1. `$ git clone https://github.com/ess3nt1al/ytdl-bot`
2. `$ pip install -r requirements.txt`
3. Create file `.env` and put your Telegram bot token inside.
   - It should look like this: `BOT_TOKEN=NNNNNNNNNN:XXXXXX_XXXXXXXXXXXXXX`
4. Make sure you have ffmpeg installed.
   - Arch: `pacman -S ffmpeg`
   - Ubuntu: `apt intall ffmpeg`
5. Run `$ python3 app.py`
