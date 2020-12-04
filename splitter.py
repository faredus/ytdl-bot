import glob
import os

from pydub.utils import mediainfo
from os import path
import subprocess

chunk_size = 49 * 8388608  # MB to binary bits


def split_audio(filename: str) -> list:
    """Splits audio into certain sized chunks"""
    bit_rate = int(mediainfo(filename)['bit_rate'])
    chunk_length = (chunk_size / bit_rate)
    ext = path.splitext(filename)[1]
    command = f'ffmpeg -i {filename} -f segment -segment_time {chunk_length} -c copy %0d{ext}'
    subprocess.run(command, shell=True)
    os.remove(filename)
    chunks = glob.glob(f'*{ext}')
    chunks.sort()
    return chunks


