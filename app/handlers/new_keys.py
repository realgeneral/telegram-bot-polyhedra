from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing


@dp.message_handler(Text(equals=["🆕 Новые ключи"]), state=UserFollowing.choose_point)
async def new_private_keys(message: types.Message, state: FSMContext):
    await UserFollowing.new_private.set()
    await message.answer("👝 *Отправьте свой private key* \n\n"
                         "_Бот не собирает и не хранит ваши личные данные или ключи. "
                         "Проект является полностью открытым и прозрачным, и его исходный код (Open Source) доступен "
                         "для всех. \n "
                         "GitHub: https://github.com/realgeneral/telegram-bot-polyhedra_",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=UserFollowing.new_private)
async def get_new_private_keys(message: types.Message, state: FSMContext):
    wait_message = await message.answer("⏳ Получаю private key...", reply_markup=ReplyKeyboardRemove())
    private_key = message.text.strip()

    await state.update_data(private_key=private_key)
    await bot.delete_message(chat_id=wait_message.chat.id,
                             message_id=wait_message.message_id)
    buttons = [
        KeyboardButton(text="⬅ Вернуться в меню"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                       resize_keyboard=True)

    await UserFollowing.wallet_menu.set()
    await message.answer("😌 *Ключи успешно записаны*",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=reply_markup)
