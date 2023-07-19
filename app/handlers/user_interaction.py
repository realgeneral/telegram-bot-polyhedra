from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    buttons = [
        KeyboardButton(text="🚀 Начать"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)

    await message.answer("Приветствую ! 🤖👋\n",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=reply_markup)
