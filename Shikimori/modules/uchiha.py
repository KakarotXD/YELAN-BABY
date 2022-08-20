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

from Shikimori import dispatcher
from Shikimori.vars import NETWORK_USERNAME
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/e5808adf6d1bc748d6440.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "voidxnetwork":
    def uchiha(update: Update, context: CallbackContext):

        TEXT = f"""
Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork),

◈ ᴠᴏɪᴅ ɪꜱ ᴀɴ ᴀɴɪᴍᴇ ʙᴀꜱᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ ꜱᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ.
 ɢᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ɪꜰ ɪᴛ ᴅʀᴀᴡꜱ ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ. ◈
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/VoidXNetwork")],
                    [
                    InlineKeyboardButton(text="【ᴜꜱᴇʀᴛᴀɢ】", url="https://t.me/VoidxNetwork/136"),
                    InlineKeyboardButton(text="【ɪɴᴅᴇx】", url="https://t.me/VoidxNetwork/15")
                    ],
                ]
            ),
        )


    uchiha_handler = CommandHandler(("void", "network", "net"), uchiha, run_async = True)
    dispatcher.add_handler(uchiha_handler)

    __help__ = """
    ──「【V๏ɪ፝֟𝔡】Network」──                         
    
  ❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "【ᴠᴏɪᴅ】"
