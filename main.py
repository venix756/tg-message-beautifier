import asyncio
from dataclasses import dataclass
from time import time

from telethon.sync import TelegramClient, events
from telethon.tl.types import PeerChannel

from config import api_id, api_hash, message, userbot, modules


@dataclass
class AppContext:
    delay: int
    result: dict


async def main(c):
    async with TelegramClient('msgbtf', api_id, api_hash) as client:
        @client.on(events.NewMessage())
        async def handler(event):
            if userbot and event.text.startswith('.'):
                return
            if isinstance(event.peer_id, PeerChannel) and not event.is_group:
                return

            if time() - c.delay > 600:
                c.result = {k: await v.get() for k, v in modules.items()}
                c.delay = time()

            await event.edit(message.format(**c.result, messageText=event.text), parse_mode='html')

        await client.run_until_disconnected()


asyncio.run(main(AppContext(0, {})))
