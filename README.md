# ytm3bot

Telegram bot for downloading music from youtube and other sites built on FFmpeg and youtube-dl.

## Requirements

- ffmpeg
- Python 3

## Installing

1. `$ git clone https://github.com/ess3nt1al/ytdl-bot`
2. `$ pip install -r requirements.txt`
3. Create file `.env` and put your Telegram bot token inside.
   - It should look like this: `BOT_TOKEN=token`
4. Make sure you have ffmpeg installed.
   - Arch: `pacman -S ffmpeg`
   - Ubuntu: `apt intall ffmpeg`
5. Run `$ python3 app.py`

## Description
Telegram bot which allows you to convert videos to mp3 files. Works with most sites, can download YouTube playlists, split large audio files into pieces to overcome api limit.
