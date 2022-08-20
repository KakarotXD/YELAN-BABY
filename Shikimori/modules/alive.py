"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

from Shikimori.vars import ALIVE_MEDIA, UPDATE_CHANNEL, SUPPORT_CHAT, OWNER_USERNAME, NETWORK, NETWORK_USERNAME
from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s

bot_name = f"{dispatcher.bot.first_name}"

ALIVE_ID = ALIVE_MEDIA.split(".")
alive_id = ALIVE_ID[-1]

def awake(update: Update, context: CallbackContext):
    message = update.effective_message
    buttons = [
        [
        InlineKeyboardButton(
            text="【Uᴘᴅᴀᴛᴇ】",
            url=f"https://t.me/YelanXUpdates"),
        InlineKeyboardButton(
            text="【Sᴜᴘᴘᴏʀᴛ】",
            url=f"https://t.me/YelanXjinWoo"),
        ],
     ]
    
    first_name = update.effective_user.first_name
    user = message.from_user

    TEXT = f"""
✪ Hᴏɪɪ <a href="tg://user?id={user.id}">{first_name}</a>,

✪ I'ᴍ ᴡᴏʀᴋɪɴɢ ᴡɪᴛʜ ᴇᴠᴇʀʏᴛʜɪɴɢ ɪ'ᴠᴇ ɢᴏᴛ.

━━━━━━━━━━━━━━━━━━━━━━>
❍ My Devloper - [S U N G • J I N • W O O](tg://user?id=1054969108)

➢ Python Version : `{y()}`
➢ Library Version : `{o}` 
➢ Telethon Version : `{s}` 
➢ Pyrogram Version : `{z}`
━━━━━━━━━━━━━━━━━━━━━━━>
    """
    if NETWORK:
        TEXT = TEXT + f"""\n✭ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :  [V๏ɪ፝֟𝔡 ɴᴇᴛᴡᴏʀᴋ](http://t.me/voidxnetwork)\n' + '✪ Tʜᴀɴᴋꜱ Fᴏʀ Aᴅᴅɪɴɢ Me Hᴇʀᴇ
"""
    
    else:
        TEXT = TEXT + "\n enter network name "

    try:
        if alive_id in ("jpeg", "jpg", "png"):
            message.reply_photo(ALIVE_MEDIA, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)
        elif alive_id in ("mp4", "mkv"):
            message.reply_video(ALIVE_MEDIA, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)
        elif alive_id in ("gif", "webp"):
            message.reply_animation(ALIVE_MEDIA, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)
        else:
            message.reply_text(TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)

    except:
        message.reply_text(TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)

ALIVE_HANDLER = DisableAbleCommandHandler("alive", awake, run_async=True)
dispatcher.add_handler(ALIVE_HANDLER)
__command_list__ = ["alive"]
__handlers__ = [
    ALIVE_HANDLER,
]

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
