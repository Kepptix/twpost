import json

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter, Command 
from aiogram.types import Message

router = Router()

class ChangeSettings(StatesGroup):
    change_channel = State()
    change_user = State()

@router.message(Command("settings"))
async def settings_cmd(m: Message):
    with open('settings.json', 'r') as file:
        settings = json.load(file)

    text = "Bot settings\n"

    for setting in settings:
        text += f"\n{setting.capitalize()}: <code>{settings.get(setting)}</code>"
    
    await m.answer(text)

@router.message(Command("change_user"))
async def change_user_cmd(m: Message, state: FSMContext):
    await m.answer("Enter user twitch nickname")
    await state.set_state(ChangeSettings.change_user)

@router.message(StateFilter(ChangeSettings.change_user))
async def change_user_state(m: Message, state: FSMContext):
    user = m.text.split(' ')[0]
    
    with open('settings.json', 'r') as file:
        settings = json.load(file)
        settings['user'] = user

    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=4)

    await m.answer(f"User changed to <code>{user}</code>")
    await state.clear()

@router.message(Command("change_channel"))
async def change_channel_cmd(m: Message, state: FSMContext):
    await m.answer("Enter channel id ")
    await state.set_state(ChangeSettings.change_channel)

@router.message(StateFilter(ChangeSettings.change_channel))
async def change_channel_state(m: Message, state: FSMContext):
    channel = int('-100' + m.text.split(" ")[0]) if m.text.split(' ')[0][0:4] != "-100" else m.text.split(' ')[0]

    with open('settings.json', 'r') as file:
        settings = json.load(file)
        settings['channel'] = channel

    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=4)

    await m.answer(f"Channel changed to <code>{channel}</code>")
    await state.clear()
    