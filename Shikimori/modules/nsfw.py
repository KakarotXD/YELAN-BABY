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

import html
import time
import requests
from pyrogram import filters
import nekos
from Shikimori.imports.hmfull.src import hmfull
from Shikimori import dispatcher, pbot
from Shikimori.vars import SUPPORT_CHAT
import Shikimori.modules.mongo.nsfw_mongo as sql
from Shikimori.modules.log_channel import gloggable
from telegram import Update
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CommandHandler, CallbackContext
from Shikimori.modules.helper_funcs.filters import CustomFilters
from Shikimori.modules.helper_funcs.chat_status import user_admin
from telegram.utils.helpers import mention_html
url_nsfw = "https://api.waifu.pics/nsfw/"

@user_admin
@gloggable
def add_nsfw(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        sql.set_nsfw(chat.id)
        msg.reply_text("Activated NSFW Mode!")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"ACTIVATED_NSFW\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message
    else:
        msg.reply_text("NSFW Mode is already Activated for this chat!")
        return ""

@user_admin
@gloggable
def rem_nsfw(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        msg.reply_text("NSFW Mode is already Deactivated")
        return ""
    else:
        sql.rem_nsfw(chat.id)
        msg.reply_text("Rolled Back to SFW Mode!")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"DEACTIVATED_NSFW\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message

def blowjob(update, context):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            msg.reply_text("NSFW is not activated!!\n\nUse '/addnsfw' to activate NSFW commands.")
            return
    url = f"{url_nsfw}blowjob" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def trap(update, context):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            msg.reply_text("NSFW is not activated!!\n\nUse '/addnsfw' to activate NSFW commands.")
            return
    url = f"{url_nsfw}trap" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def nsfwwaifu(update, context):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            msg.reply_text("NSFW is not activated!!\n\nUse '/addnsfw' to activate NSFW commands.")
            return
    url = f"{url_nsfw}waifu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def nsfwneko(update, context):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            msg.reply_text("NSFW is not activated!!\n\nUse '/addnsfw' to activate NSFW commands.")
            return
    url = f"{url_nsfw}neko" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def spank(update, context):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    target = "spank"
    msg.reply_animation(nekos.img(target))

ADD_NSFW_HANDLER = CommandHandler("addnsfw", add_nsfw)
REMOVE_NSFW_HANDLER = CommandHandler("rmnsfw", rem_nsfw)
NSFWWAIFU_HANDLER = CommandHandler(("nsfwwaifu", "nwaifu"), nsfwwaifu, run_async=True)
BLOWJOB_HANDLER = CommandHandler(("blowjob", "bj"), blowjob, run_async=True)
TRAP_HANDLER = CommandHandler("trap", trap, run_async=True)
NSFWNEKO_HANDLER = CommandHandler(("nsfwneko", "nneko"), nsfwneko, run_async=True)
SPANK_HANDLER = CommandHandler("spank", spank, run_async=True)

dispatcher.add_handler(ADD_NSFW_HANDLER)
dispatcher.add_handler(REMOVE_NSFW_HANDLER)
dispatcher.add_handler(NSFWWAIFU_HANDLER)
dispatcher.add_handler(BLOWJOB_HANDLER)
dispatcher.add_handler(SPANK_HANDLER)
dispatcher.add_handler(TRAP_HANDLER)
dispatcher.add_handler(NSFWNEKO_HANDLER)

__handlers__ = [
    ADD_NSFW_HANDLER,
    REMOVE_NSFW_HANDLER,
    NSFWWAIFU_HANDLER,
    SPANK_HANDLER,
    BLOWJOB_HANDLER,
    TRAP_HANDLER,
    NSFWNEKO_HANDLER
]



__mod_name__ = "「 NSFW 」"

__help__ = """
❍ `/addnsfw` : To Activate NSFW commands.
❍ `/rmnsfw` : To Deactivate NSFW commands.

❍ `/nsfw` ['ass', 'bdsm', 'cum', 'creampie', 'manga', 'blowjob', 'bj', 'boobjob', 'vagina', 'uniform', 'foot', 'femdom', 'gangbang', 'hentai', 'incest', 'ahegao', 'neko', 'gif', 'ero', 'cuckold', 'orgy', 'elves', 'pantsu', 'mobile', 'glasses', 'tentacles', 'tentacle', 'thighs', 'yuri', 'zettai', 'masturbation', 'public', 'wallpaper', 'nekolewd', 'nekogif', 'henti', 'hass', 'boobs', 'paizuri', 'hyuri', 'hthigh', 'midriff', 'kitsune', 'tentacle', 'anal', 'hanal', 'hneko']

Following are the NSFW commands:

    ➢ `/nsfwwaifu`
    ➢ `/blowjob`
    ➢ `/nwaifu`
    ➢ `/bj`
    ➢ `/trap`
    ➢ `/nsfwneko`
    ➢ `/nneko`
    ➢ `/spank`
"""

@pbot.on_message(filters.command('nsfw'))
async def ass(_, message):
    chat_id = message.chat.id
    nsfw_query = ["ass", "cum", "creampie", "manga", "blowjob", "bj", "boobjob", "vagina", "uniform", "foot", "femdom", "gangbang", "hentai", "incest", "ahegao", "neko", "gif", "ero", "cuckold", "orgy", "elves", "pantsu", "mobile", "glasses", "tentacles", "tentacle", "thighs", "yuri", "zettai", "masturbation", "public", "wallpaper", "nekolewd", "nekogif", "henti", "hass", "boobs", "paizuri", "hyuri", "hthigh", "midriff", "kitsune", "tentacle", "anal", "hanal", "hneko"]
    if not message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            await message.reply_text("NSFW is not activated!!\n\nUse '/addnsfw' to activate NSFW commands.")
            return
    for ch in ["[", "]", "'"]:
        h = f"{nsfw_query}"
        if ch in h:
            n_query = h.replace(ch, "") 
        else:
            n_query = nsfw_query
    if len(message.command) != 2:
        return await message.reply_text(
            f"Usage: /nsfw `{n_query}`"
        )
    query = message.text.split(None, 1)[1].strip()
    query = query.lower()
    try:
        if query in nsfw_query: 
            if query == "ass":
                res = hmfull.HMtai.nsfw.ass()
            elif query == "cum":
                res = hmfull.HMtai.nsfw.cum()
            elif query == "creampie":
                res = hmfull.HMtai.nsfw.creampie()
            elif query == "manga":
                res = hmfull.HMtai.nsfw.manga()
            elif query == "blowjob" or query =="bj":
                res = hmfull.HMtai.nsfw.blowjob()
            elif query == "boobjob":
                res = hmfull.HMtai.nsfw.boobjob()
            elif query == "vagina":
                res = hmfull.HMtai.nsfw.vagina()
            elif query == "uniform":
                res = hmfull.HMtai.nsfw.uniform()
            elif query == "foot":
                res = hmfull.HMtai.nsfw.foot()
            elif query == "femdom":
                res = hmfull.HMtai.nsfw.femdom()
            elif query == "gangbang":
                res = hmfull.HMtai.nsfw.gangbang()
            elif query == "hentai":
                res = hmfull.HMtai.nsfw.hentai()
            elif query == "incest":
                res = hmfull.HMtai.nsfw.incest()
            elif query == "ahegao":
                res = hmfull.HMtai.nsfw.ahegao()
            elif query == "neko":
                res = hmfull.HMtai.nsfw.neko()
            elif query == "gif":
                hmm = hmfull.HMtai.nsfw.gif()
                url = hmm["url"]
                return await message.reply_animation(url)
            elif query == "ero":
                res = hmfull.HMtai.nsfw.ero()
            elif query == "cuckold":
                res = hmfull.HMtai.nsfw.cuckold()
            elif query == "orgy":
                res = hmfull.HMtai.nsfw.orgy()
            elif query == "elves":
                res = hmfull.HMtai.nsfw.elves()
            elif query == "pantsu":
                res = hmfull.HMtai.nsfw.pantsu()
            elif query == "mobile":
                res = hmfull.HMtai.nsfw.nsfwMobileWallpaper()
            elif query == "glasses":
                res = hmfull.HMtai.nsfw.glasses()
            elif query == "tentacles":
                res = hmfull.HMtai.nsfw.tentacles()
            elif query == "thighs":
                res = hmfull.HMtai.nsfw.thighs()
            elif query == "yuri":
                res = hmfull.HMtai.nsfw.yuri()
            elif query == "zettai":
                res = hmfull.HMtai.nsfw.zettaiRyouiki()
            elif query == "masturbation":
                res = hmfull.HMtai.nsfw.masturbation()
            elif query == "public":
                res = hmfull.HMtai.nsfw.public()
            elif query == "wallpaper":
                res = hmfull.Nekos.nsfw.wallpaper()
            elif query == "nekolewd":
                res = hmfull.NekoLove.nsfw.nekolewd()
            elif query == "nekogif":
                hmm = hmfull.Nekos.nsfw.nekogif()
                url = hmm["url"]
                return await message.reply_animation(url)
            elif query == "henti":
                res = hmfull.NekoBot.nsfw.hentai()
            elif query == "hass":
                res = hmfull.NekoBot.nsfw.hass()
            elif query == "boobs":
                res = hmfull.NekoBot.nsfw.boobs()
            elif query == "paizuri":
                res = hmfull.NekoBot.nsfw.paizuri()
            elif query == "hyuri":
                res = hmfull.NekoBot.nsfw.yuri()
            elif query == "hthigh":
                res = hmfull.NekoBot.nsfw.thigh()
            elif query == "midriff":
                res = hmfull.NekoBot.nsfw.midriff()
            elif query == "kitsune":
                res = hmfull.NekoBot.nsfw.kitsune()
            elif query == "tentacle":
                res = hmfull.NekoBot.nsfw.tentacle()
            elif query == "anal":
                res = hmfull.NekoBot.nsfw.anal()
            elif query == "hanal":
                res = hmfull.NekoBot.nsfw.hanal()
            elif query == "hneko":
                res = hmfull.NekoBot.nsfw.hneko()

            url = res["url"]
            return await message.reply_photo(url)
        else:
            return await message.reply_text(f"Usage: /nsfw `{n_query}`")
    except:
        return await message.reply_text(f"ERROR!!! Contact @{SUPPORT_CHAT}")


