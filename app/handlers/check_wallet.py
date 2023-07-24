from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing
from app.utils import Balance


@dp.message_handler(Text(equals=["👝 Проверить баланс"]), state=UserFollowing.choose_point)
async def check_wallet_keys(message: types.Message, state: FSMContext):
    url_bnb = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd"
    url_polygon = "https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=usd"
    url_core = ""
    url_celo = "https://api.coingecko.com/api/v3/simple/price?ids=celo&vs_currencies=usd"

    data = await state.get_data()
    private_key = data.get("private_key")

    wait_1_message = await message.answer("⏳ Получаю информацию о кошельке 0%")
    bsc = Balance(private_key, 'bsc', "binancecoin")
    bsc_balance = await bsc.get_balance(url_bnb)

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text="⏳ Получаю информацию о кошельке 25%")

    polygon = Balance(private_key, 'polygon', "matic-network")
    polygon_balance = await polygon.get_balance(url_polygon)

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text="⏳ Получаю информацию о кошельке 50%")

    core = Balance(private_key, 'core', "core")
    core_balance = await core.get_balance(url_core)

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text="⏳ Получаю информацию о кошельке 75%")

    celo = Balance(private_key, 'celo', "celo")
    celo_balance = await celo.get_balance(url_celo)

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text="⏳ Получаю информацию о кошельке 100%")

    if bsc_balance == -6:
        bsc_balance_str = "❌ Произошла ошибка"
    elif bsc_balance[0] >= 0.02065:
        bsc_balance_str = f"{bsc_balance[0]}(= {bsc_balance[1]}$) ✅ - Достаточно для оплаты газа"
    else:
        bsc_balance_str = f"{bsc_balance[0]}(= {bsc_balance[1]}$) ❌ - Недостаточно для оплаты газа"

    if polygon_balance == -6:
        polygon_balance_str = "❌ Произошла ошибка"
    elif polygon_balance[0] >= 3.1:
        polygon_balance_str = f"{polygon_balance[0]}(= {polygon_balance[1]}$) ✅  - Достаточно для оплаты газа"
    else:
        polygon_balance_str = f"{polygon_balance[0]}(= {polygon_balance[1]}$) ❌ - Недостаточно для оплаты газа"

    if core_balance == -6:
        core_balance_str = "❌ Произошла ошибка"
    elif core_balance[0] >= 2.5:
        core_balance_str = f"{core_balance[0]} ✅ - Достаточно для оплаты газа"
    else:
        core_balance_str = f"{core_balance[0]} ❌ - Недостаточно для оплаты газа"

    if celo_balance == -6:
        celo_balance_str = "❌ Произошла ошибка"
    elif celo_balance[0] >= 2.5:
        celo_balance_str = f"{celo_balance[0]}(= {celo_balance[1]}$) ✅ - Достаточно для оплаты газа"
    else:
        celo_balance_str = f"{celo_balance[0]}(= {celo_balance[1]}$) ❌  Недостаточно для оплаты газа"

    buttons = [
        KeyboardButton(text="⬅ Вернуться в меню"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                       resize_keyboard=True)

    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)
    await UserFollowing.wallet_menu.set()
    await message.answer(f" 📊 <b> Баланс </b> \n\n"
                         f"<u>BNB</u>  = {bsc_balance_str}\n"
                         f"<u>MATIC</u> = {polygon_balance_str}\n"
                         f"<u>Core</u> = {core_balance_str}\n"
                         f"<u>Celo</u> = {celo_balance_str}\n", parse_mode=types.ParseMode.HTML,
                         reply_markup=reply_markup)

