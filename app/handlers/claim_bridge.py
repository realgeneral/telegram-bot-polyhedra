import asyncio

from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing
from app.utils import Bridger


@dp.message_handler(Text(equals="💸 Кроссчейн nft сендер"), state=UserFollowing.choose_point)
async def claim_bridge(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")
    api_key = data.get("api_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю бридж nft 0/7")

    zklight_bridger = Bridger(private_key, 'ZkLightClient', 'bsc', 'opbnb')
    is_zklight_bridge = await zklight_bridger.bridge(api_key)
    if is_zklight_bridge == -2:
        is_zklight_bridge = ["❌ Не хватает газа", ""]
    elif is_zklight_bridge == -3:
        is_zklight_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_zklight_bridge == -4:
        is_zklight_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_zklight_bridge == -6:
        is_zklight_bridge = ["❌ Произошла ошибка", ""]

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 1/7")

    opbnb_bridger = Bridger(private_key, 'ZkBridge on opBNB', 'bsc', 'opbnb')
    is_opbnb_bridge = await opbnb_bridger.bridge(api_key)
    if is_opbnb_bridge == -2:
        is_opbnb_bridge = ["❌ Не хватает газа", ""]
    elif is_opbnb_bridge == -3:
        is_opbnb_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_opbnb_bridge == -4:
        is_opbnb_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_opbnb_bridge == -6:
        is_opbnb_bridge = ["❌ Произошла ошибка", ""]

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 2/7")

    core_bridger = Bridger(private_key, 'Mainnet Alpha', 'core', 'polygon')
    is_core_bridge = await core_bridger.bridge(api_key)
    if is_core_bridge == -2:
        is_core_bridge = ["❌ Не хватает газа", ""]
    elif is_core_bridge == -3:
        is_core_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_core_bridge == -4:
        is_core_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_core_bridge == -6:
        is_core_bridge = ["❌ Произошла ошибка", ""]

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 3/7")

    pandra_bsc_bridger = Bridger(private_key, 'Pandra', 'bsc', 'core')
    is_pandra_bsc_bridge = await pandra_bsc_bridger.bridge(api_key)
    if is_pandra_bsc_bridge == -2:
        is_pandra_bsc_bridge = ["❌ Не хватает газа", ""]
    elif is_pandra_bsc_bridge == -3:
        is_pandra_bsc_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_pandra_bsc_bridge == -4:
        is_pandra_bsc_bridge = "❌ Что-то пошло не так, попробуйте заново"
    elif is_pandra_bsc_bridge == -6:
        is_pandra_bsc_bridge = ["❌ Произошла ошибка", ""]

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 4/7")

    pandra_polygon_bridger = Bridger(private_key, 'Pandra', 'polygon', 'bsc')
    is_pandra_pol_bridge = await pandra_polygon_bridger.bridge(api_key)
    if is_pandra_pol_bridge == -2:
        is_pandra_pol_bridge = ["❌ Не хватает газа", ""]
    elif is_pandra_pol_bridge == -3:
        is_pandra_pol_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_pandra_pol_bridge == -4:
        is_pandra_pol_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_pandra_pol_bridge == -6:
        is_pandra_pol_bridge = ["❌ Произошла ошибка", ""]

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 5/7")

    pandra_core_bridger = Bridger(private_key, 'Pandra', 'core', 'polygon')
    is_pandra_core_bridge = await pandra_core_bridger.bridge(api_key)
    if is_pandra_core_bridge == -2:
        is_pandra_core_bridge = ["❌ Не хватает газа", ""]
    elif is_pandra_core_bridge == -3:
        is_pandra_core_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_pandra_core_bridge == -4:
        is_pandra_core_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_pandra_core_bridge == -6:
        is_pandra_core_bridge = ["❌ Произошла ошибка", ""]

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 6/7")

    pandra_celo_bridger = Bridger(private_key, 'Pandra', 'celo', 'bsc')
    is_pandra_celo_bridge = await pandra_celo_bridger.bridge(api_key)
    if is_pandra_celo_bridge == -2:
        is_pandra_celo_bridge = ["❌ Не хватает газа", ""]
    elif is_pandra_celo_bridge == -3:
        is_pandra_celo_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_pandra_celo_bridge == -4:
        is_pandra_celo_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_pandra_celo_bridge == -6:
        is_pandra_celo_bridge = ["❌ Произошла ошибка", ""]

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 7/7")
    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)
    buttons = [
        KeyboardButton(text="⬅ Вернуться в меню"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                       resize_keyboard=True)
    await UserFollowing.wallet_menu.set()
    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Кроссчейн nft сендер (Blockchain:Transaction Hash)</u> \n"
                         f'  🔘 <i> ZkLightClient nft </i> {is_zklight_bridge[0]}<code>{is_zklight_bridge[1]}</code> \n'
                         f'  🔘 <i> ZkBridge on opBNB nft </i> {is_opbnb_bridge[0]}<code>{is_opbnb_bridge[1]}</code> \n'
                         f'  🔘 <i> Mainnet Alpha nft </i> {is_core_bridge[0]}<code>{is_core_bridge[1]}</code> \n'
                         f'  🔘 <i> CodeConqueror (Pandra) nft </i> {is_pandra_bsc_bridge[0]}<code>{is_pandra_bsc_bridge[1]}</code>\n'
                         f'  🔘 <i> PixelProwler (Pandra) nft </i> {is_pandra_pol_bridge[0]}<code>{is_pandra_pol_bridge[1]}</code> \n'
                         f'  🔘 <i> MelodyMaven (Pandra) nft </i> {is_pandra_core_bridge[0]}<code>{is_pandra_core_bridge[1]}</code>\n'
                         f'  🔘 <i> EcoGuardian (Pandra) nft </i> {is_pandra_celo_bridge[0]}<code>{is_pandra_celo_bridge[1]}</code>\n\n',
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=reply_markup)
