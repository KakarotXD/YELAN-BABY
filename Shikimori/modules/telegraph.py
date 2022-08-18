"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from Shikimori.events import register
from Shikimori import telethn as tbot
from telegram import ParseMode  
TMP_DOWNLOAD_DIRECTORY = "./"
import os
from PIL import Image
from datetime import datetime
from telegraph import Telegraph, upload_file, exceptions
Hero = "Shikimori"
telegraph = Telegraph()
r = telegraph.create_account(short_name=Hero)
auth_url = r["auth_url"]


@register(pattern="^/t(gm|gt) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "gm":
            downloaded_file_name = await tbot.download_media(
                r_message,
                TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            h = await event.reply("Downloaded to {} in {} seconds.".format(downloaded_file_name, ms))
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await h.edit("ERROR: " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await h.edit("[Telegraph Link](https://telegra.ph{}) `https://telegra.ph{}`".format(media_urls[0], media_urls[0]), link_preview=True, parse_mode=ParseMode.MARKDOWN)
        elif input_str == "gt":
            user_object = await tbot.get_entity(r_message.sender_id)
            title_of_page = user_object.first_name # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await tbot.download_media(
                    r_message,
                    TMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(
                title_of_page,
                html_content=page_content
            )
            end = datetime.now()
            ms = (end - start).seconds
            await event.reply("Telegraph Link- [Click Here](https://telegra.ph/{}) in {} seconds.".format(response["path"], ms), link_preview=True, parse_mode=ParseMode.MARKDOWN)
    else:
        await event.reply("Reply to a message to get a permanent telegra.ph link.")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


__help__ = """
I can upload files to Telegraph

 • `/tgm` :Get Telegraph Link Of Replied Media.
 • `/tgt` :Get Telegraph Link of Replied Text.
"""

__mod_name__ = "Telegraph"
