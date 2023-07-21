from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp
from app.states import UserFollowing


@dp.message_handler(Text(equals=["🔑 Проверить ключи"]), state=UserFollowing.choose_point)
async def new_private_keys(message: types.Message, state: FSMContext):
    data = await state.get_data()
    private_key = data.get("private_key")
    api_key = data.get("api_key")

    await message.answer(f"# Private key *{private_key[0:6]}...{private_key[-4:]}* \n"
                         f"# API key *{api_key[0:6]}...{api_key[-4:]}*\n\n", parse_mode=types.ParseMode.MARKDOWN)
    await UserFollowing.choose_point.set()
