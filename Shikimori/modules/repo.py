from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from Shikimori import pbot as client


ANON = "https://telegra.ph/file/2e4707e6c618e468a2373.jpg"

@client.on_message(filters.command(["repo", "source" , "owner"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**Hᴇʏ** {message.from_user.mention()},\n**Its Me The Bot Owner**

❍ Owner - [S U N G • J I N • W O O ](tg://user?id=1054969108)


➢ Python Version : `{y()}`
➢ Library Version : `{o}` 
➢ Telethon Version : `{s}` 
➢ Pyrogram Version : `{z}`

✪ Powered By - [【V๏ɪ፝֟𝔡】◈Network◈](t.me/voidxnetwork)

 *My policy decline your request for the repo.*
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="tg://user?id=1054969108"), 
                    InlineKeyboardButton(
                        "Void Network", url="https://t.me/voidxnetwork")
                ]
            ]
        )
    )

__mod_name__ = "Repo/Source"
