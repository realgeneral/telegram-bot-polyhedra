from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing
from app.utils import Messager


@dp.message_handler(Text(equals="📩 Отправка сообщения"), state=UserFollowing.choose_point)
async def claim_message(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Отправляю сообщение ...")

    is_sending = await Messager.messsage(private_key)
    if is_sending == -2:
        is_sending = "❌ Не хватает газа"
    elif is_sending == -6:
        is_sending = "❌ Произошла ошибка"
    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)
    buttons = [
        KeyboardButton(text="⬅ Вернуться в меню"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                       resize_keyboard=True)
    await UserFollowing.wallet_menu.set()
    await message.answer("📊 <b>Статистика</b> \n\n"
                         '<u>Отправка сообщения (zkMessenger): </u> \n'
                         f'  🔘 <i> из BSC в Polygon </i> {is_sending} \n\n',
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=reply_markup)
