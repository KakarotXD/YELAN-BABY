# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from __future__ import unicode_literals

import asyncio
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import wget
import yt_dlp as youtube_dl
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

from Shikimori import arq
from Shikimori.utils.pluginhelper import get_text, progress
from Shikimori import pbot as Client

dl_limit = 0


@Client.on_message(filters.command(["music", "song"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)
    if not urlissed:
        await client.send_message(
            message.chat.id,
            "Invalid Command Syntax, Please Check Help Menu To Know More!",
        )
        return
    global dl_limit
    if dl_limit >= 4:
        await message.reply_text(
            "Too many request, please try again after sometime."
        )
        return
    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    try:
        mi = search.result()
        mio = mi["search_result"]
        mo = mio[0]["link"]
        mio[0]["duration"]
        thum = mio[0]["title"]
        fridayz = mio[0]["id"]
        thums = mio[0]["channel"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    except:
        await message.reply_text(
            "Sorry I accounted an error.\n Unkown error raised while getting search result"
        )
        return

    await asyncio.sleep(0.6)
    sedlyf = wget.download(kekme)
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "720",
            }
        ],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    try:
        dl_limit = dl_limit + 1
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)

    except Exception as e:
        await pablo.edit_text(f"**Failed To Download** \n**Error :** `{str(e)}`")
        # dl_limit = dl_limit-1
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp3"
    try:
        await client.send_audio(
            message.chat.id,
            audio=open(file_stark, "rb"),
            duration=int(ytdl_data["duration"]),
            title=str(ytdl_data["title"]),
            performer=str(ytdl_data["uploader"]),
            thumb=sedlyf,
            progress=progress,
            progress_args=(
                pablo,
                c_time,
                f"`Uploading {urlissed} Song From YouTube Music!`",
                file_stark,
            ),
        )
        dl_limit = dl_limit - 1
    except:
        dl_limit = dl_limit - 1
        return
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


ydl_opts = {
    "format": "bestaudio/best",
    "writethumbnail": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


# Funtion To Download Song
async def download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


is_downloading = False


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


@Client.on_message(filters.command(["vsong", "video"]))
async def ytmusic(client, message: Message):
    global is_downloading
    if is_downloading:
        await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
        return
    global dl_limit
    if dl_limit >= 4:
        await message.reply_text(
            "Too many requests, please try again after sometime.."
        )
        return
    urlissed = get_text(message)

    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    if not urlissed:
        await pablo.edit_text("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    try:
        mi = search.result()
        mio = mi["search_result"]
        mo = mio[0]["link"]
        thum = mio[0]["title"]
        fridayz = mio[0]["id"]
        thums = mio[0]["channel"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    except:
        await message.reply_text(
            "Unknown error raised while getting result from youtube"
        )
        return
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        is_downloading = True
        with youtube_dl.YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            duration = round(infoo["duration"] / 60)

            if duration > 8:
                await pablo.edit_text(
                    f"❌ Videos longer than 8 minute(s) aren t allowed, the provided video is {duration} minute(s)"
                )
                is_downloading = False
                return
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception:
        # await pablo.edit_text(event, f"**Failed To Download** \n**Error :** `{str(e)}`")
        is_downloading = False
        return

    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{thum}` \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` \n**Link :** `{mo}`"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`Uploading {urlissed} Song From YouTube Music!`",
            file_stark,
        ),
    )
    await pablo.delete()
    is_downloading = False
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)

__mod_name__ = "Song 🎵"

__help__ = """
> `/song` <songname> *:* To download a song. (Works with Youtube link too)
> `/music` <songname> *:* To download a song. (Works with Youtube link too)
> `/video` <videoname> or Youtube Link> *:* To download a video.
> `/vsong` <videoname> or Youtube Link> *:* To download a video.
"""
