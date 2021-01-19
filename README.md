# ytdl-bot

Telegram bot for audio downloading. Built on FFmpeg and youtube-dl. Works with most sites, can download YouTube playlists, uses pyrogram to overcome Telegram Bot API file size limits.

## Requirements

- ffmpeg
- Python 3.7

## Installing

1. `$ git clone https://github.com/ess3nt1al/ytdl-bot`
2. `$ pip install -r requirements.txt`
3. Put your Telegram bot token, api id, api hash into `.env`
4. Make sure you have ffmpeg installed.
   - Arch: `pacman -S ffmpeg`
   - Ubuntu: `apt intall ffmpeg`
5. Run `$ python3 app.py`
