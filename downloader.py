from youtube_dl import YoutubeDL


ydl_opts = {
    "verbose": True,
    "format": "bestaudio/worst",
    "outtmpl": "track.%(ext)s",
    "cachedir": False,
    "noplaylist": True,
    "ignoreerrors": True,
    "youtube_include_dash_manifest": False,
    "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "opus"}],
}


async def download(url: str, options: dict) -> str:
    """Downloads file, converts it if needed, returns track title"""
    ydl_opts["postprocessors"][0]["preferredcodec"] = options["codec"]
    if options["bit_rate"] == "original":
        ydl_opts["postprocessors"][0]["preferredquality"] = None
    else:
        ydl_opts["postprocessors"][0]["preferredquality"] = options["bit_rate"]

    with YoutubeDL(ydl_opts) as ydl:
        # Call coro from here pls
        info = ydl.extract_info(url)
        return info["title"]


def handle_playlist(url: str) -> list:
    """Converts youtube playlist link in a list of urls"""
    tracks = []
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if not info:
            raise Exception("Track not found")
        for entry in info["entries"]:
            if entry is not None:
                tracks.append("https://www.youtube.com/watch?v=" + entry["id"])
    return tracks
