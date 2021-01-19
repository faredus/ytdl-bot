import asyncio
import os
from dotenv import load_dotenv

from pyrogram import Client
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import NetworkError
from validator_collection import checkers

from downloader import handle_playlist, download

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
app = Client("my_account", API_ID, API_HASH)

callback = CallbackData("options", "codec", "bit_rate")


class States(StatesGroup):
    url = State()
    upload = State()


@dp.message_handler(CommandStart(), CommandHelp(), state="*")
async def display_help(message: Message):
    await message.answer(
        "This bot can:\n"
        "- Download videos from YouTube and other sites and send them to you in audio format.\n"
        "- Download YouTube playlists.\n"
        "- Convert audio files to different formats.\n\n"
        "Just send a link (for YouTube, you can do that via @vid)\n"
    )


def get_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="mp3", callback_data=callback.new(codec="mp3", bit_rate="original")
        ),
        InlineKeyboardButton(
            text="opus", callback_data=callback.new(codec="opus", bit_rate="original")
        ),
        InlineKeyboardButton(
            text="m4a", callback_data=callback.new(codec="m4a", bit_rate="original")
        ),
    )
    markup.row(
        InlineKeyboardButton(
            text="mp3/32", callback_data=callback.new(codec="mp3", bit_rate="32")
        )
    )

    return markup


async def send_audio(chat_id, audio, title):
    await app.send_audio(chat_id=chat_id, audio=audio, title=title)


@dp.message_handler(state="*")
async def handle_url(message: Message, state: FSMContext):
    if checkers.is_url(message.text):
        await States.url.set()
        await state.update_data(url=message.text)
        markup = get_keyboard()
        await message.answer("Options:", reply_markup=markup)
    else:
        await message.answer("Invalid link.")


@dp.callback_query_handler(callback.filter(), state=States.url)
async def inline_options(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.edit_text("Please wait...")
    state_data = await state.get_data()
    url = state_data["url"]
    filename = "track." + callback_data["codec"]

    try:
        if "list" in url:
            tracks = handle_playlist(url)
            for t in tracks:
                title = download(t, callback_data)
                await send_audio(call.message.chat.id, open(filename, "rb"), title)
        else:
            title = await download(url, callback_data)
            await send_audio(call.message.chat.id, open(filename, "rb"), title)
        os.remove(filename)
    except:
        await call.message.edit_text("Something went wrong...")
    finally:
        await state.finish()





