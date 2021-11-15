import asyncio
import os
from datetime import datetime

from telethon import events


from .. import ALIVE_NAME
from ..cmdhelp import CmdHelp
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    start = datetime.now()
    event = await edit_or_reply(event, "**(❛ ᑭσɳց ❜!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    if LEGEND_IMG:
        legend_caption = (
            f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE_NAME}』"
        )
        await tgbot.send_message(event.chat_id, LEGEND_IMG, caption=legend_caption)
