import asyncio
from contextlib import suppress
import os
import json

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties 
from aiogram.enums import ParseMode

from twitchAPI.twitch import Twitch

from src.data import config
from src.handlers import register_routers

router = Router()

if not os.path.exists("settings.json"):
    with open("settings.json", 'w') as file:
        settings = {"channel": None, "user": None}
        json.dump(settings, file, indent=4)

async def main():
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    twitch = await Twitch(app_id=config.APP_ID, app_secret=config.APP_SECRET)
    dp['twitch'] = twitch

    dp.startup.register(on_start)
    dp.shutdown.register(on_stop)

    dp.include_router(register_routers(router))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
async def on_start():
    print("Bot started")

async def on_stop():
    print("Bot stopped")

if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())