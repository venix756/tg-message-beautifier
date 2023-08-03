from config import api_id, api_hash, start, end, userbot

from telethon.sync import TelegramClient, events
from telethon.types import Channel

with TelegramClient('msgbtf', api_id, api_hash) as client:
    @client.on(events.NewMessage())
    async def handler(event):
        if userbot and event.text.startswith('.') or isinstance(event.chat, Channel):
            return
        await event.edit(start+event.text+end, parse_mode='html')

    client.run_until_disconnected()
