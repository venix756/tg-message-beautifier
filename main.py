from config import api_id, api_hash, start, end, userbot

from telethon.sync import TelegramClient, events
from telethon.tl.types import PeerChannel

with TelegramClient('msgbtf', api_id, api_hash) as client:
    @client.on(events.NewMessage())
    async def handler(event):
        if userbot and event.text.startswith('.'):
            return
        if isinstance(event.peer_id, PeerChannel) and not event.is_group:
            return
        await event.edit(start+event.text+end, parse_mode='html')

    client.run_until_disconnected()
