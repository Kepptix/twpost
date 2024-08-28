import json

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

router = Router()

@router.message(Command("post"))
async def post_nofitication(m: Message, bot: Bot, twitch: Twitch):
    with open('settings.json', 'r') as file:
        settings = json.load(file)

    user = await first(twitch.get_users(logins=settings.get('user')))
    
    # channel = await first(twitch.search_channels(query=user.id))
    # online = True if channel.is_live else False
    # if not online:
    #     m.answer("Пользователь оффлайн\n\nОтправить? оповещение?")
    channel_information = await twitch.get_channel_information(broadcaster_id=user.id)
    title = channel_information[0].title
    
    await bot.send_message(settings.get("channel"), f"Стрим начался\n\n{title}")    
