from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp
from app.states import UserFollowing


@dp.message_handler(Text(equals=["⬅ Вернуться в меню"]), state='*')
async def go_menu(message: types.Message, state: FSMContext):
    await UserFollowing.wallet_menu.set()
    await send_menu(message, state)


@dp.message_handler(state=UserFollowing.wallet_menu)
async def send_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    private_key = data.get("private_key")
    api_key = data.get("api_key")

    b0 = KeyboardButton("👝 Проверить баланс")
    b1 = KeyboardButton("💰 Заклеймить всё")
    b2 = KeyboardButton("⛏ Минт nft")
    b3 = KeyboardButton("📩 Отправка сообщения")
    b4 = KeyboardButton("💸 Кроссчейн nft сендер")
    b5 = KeyboardButton("🆕 Новые ключи")
    b6 = KeyboardButton("🔑 Проверить ключи")

    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons.row(b0).row(b1, b2).row(b3, b4).row(b5, b6)

    await UserFollowing.choose_point.set()
    await message.answer(f"# Private key *{private_key[0:6]}...{private_key[-4:]}* \n"
                         f"# API key *{api_key[0:6]}...{api_key[-4:]}*\n\n"
                         f"Выберите действие:", parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=buttons)