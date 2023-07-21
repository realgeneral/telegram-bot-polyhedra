import asyncio

from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing
from app.utils import Bridger, Messager, Minter


@dp.message_handler(Text(equals="💰 Заклеймить всё"), state=UserFollowing.choose_point)
async def claim_all(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")
    api_key = data.get("api_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Отправляю сообщение ...")

    is_sending = Messager.messsage(private_key)
    if is_sending == -2:
        is_sending = "❌ Не хватает газа"
    elif is_sending == -6:
        is_sending = "❌ Произошла ошибка"

    await asyncio.sleep(5)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/8")

    greenfield_minter = Minter(private_key, 'bsc', 'Greenfield Testnet')
    is_gr_mint = greenfield_minter.mint()
    if is_gr_mint == -2:
        is_gr_mint = "❌ Не хватает газа"
    elif is_gr_mint == -5:
        is_gr_mint = "❌ Claimed already"
    elif is_gr_mint == -6:
        is_gr_mint = "❌ Произошла ошибка"

    await asyncio.sleep(6)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/8")

    zklight_minter = Minter(private_key, 'bsc', 'ZkLightClient')
    is_zklight_mint = zklight_minter.mint()
    if is_zklight_mint == -2:
        is_zklight_mint = "❌ Не хватает газа"
    elif is_zklight_mint == -5:
        is_zklight_mint = "❌ Claimed already"
    elif is_zklight_mint == -6:
        is_zklight_mint = "❌ Произошла ошибка"

    await asyncio.sleep(4)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 2/8")

    opbnb_minter = Minter(private_key, 'bsc', 'ZkBridge on opBNB')
    is_opbnb_mint = opbnb_minter.mint()
    if is_opbnb_mint == -2:
        is_opbnb_mint = "❌ Не хватает газа"
    elif is_opbnb_mint == -5:
        is_opbnb_mint = "❌ Claimed already"
    elif is_opbnb_mint == -6:
        is_opbnb_mint = "❌ Произошла ошибка"

    await asyncio.sleep(5)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 3/8")

    mainnetalpha_minter = Minter(private_key, 'core', 'Mainnet Alpha')
    is_main_mint = mainnetalpha_minter.mint()
    if is_main_mint == -2:
        is_main_mint = "❌ Не хватает газа"
    elif is_main_mint == -5:
        is_main_mint = "❌ Claimed already"
    elif is_main_mint == -6:
        is_main_mint = "❌ Произошла ошибка"

    await asyncio.sleep(3)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 4/8")

    pandra_bnb_minter = Minter(private_key, 'bsc', 'Pandra')
    is_pandra_bnb_mint = pandra_bnb_minter.mint()
    if is_pandra_bnb_mint == -2:
        is_pandra_bnb_mint = "❌ Не хватает газа"
    elif is_pandra_bnb_mint == -5:
        is_pandra_bnb_mint = "❌ Claimed already"
    elif is_pandra_bnb_mint == -6:
        is_pandra_bnb_mint = "❌ Произошла ошибка"

    await asyncio.sleep(5)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 5/8")

    pandra_pol_minter = Minter(private_key, 'polygon', 'Pandra')
    is_pandra_pol_mint = pandra_pol_minter.mint()
    if is_pandra_pol_mint == -2:
        is_pandra_pol_mint = "❌ Не хватает газа"
    elif is_pandra_pol_mint == -5:
        is_pandra_pol_mint = "❌ Claimed already"
    elif is_pandra_pol_mint == -6:
        is_pandra_pol_mint = "❌ Произошла ошибка"

    await asyncio.sleep(7)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 6/8")

    pandra_core_minter = Minter(private_key, 'core', 'Pandra')
    is_pandra_core_mint = pandra_core_minter.mint()
    if is_pandra_core_mint == -2:
        is_pandra_core_mint = "❌ Не хватает газа"
    elif is_pandra_core_mint == -5:
        is_pandra_core_mint = "❌ Claimed already"
    elif is_pandra_core_mint == -6:
        is_pandra_core_mint = "❌ Произошла ошибка"

    await asyncio.sleep(5)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 7/8")

    pandra_celo_minter = Minter(private_key, 'celo', 'Pandra')
    is_pandra_celo_mint = pandra_celo_minter.mint()
    if is_pandra_celo_mint == -2:
        is_pandra_celo_mint = "❌ Не хватает газа"
    elif is_pandra_celo_mint == -5:
        is_pandra_celo_mint = "❌ Claimed already"
    elif is_pandra_celo_mint == -6:
        is_pandra_celo_mint = "❌ Произошла ошибка"

    await asyncio.sleep(4)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 8/8. Приступаю к бриджу nft 0/7")

    zklight_bridger = Bridger(private_key, 'ZkLightClient', 'bsc', 'opbnb')
    is_zklight_bridge = zklight_bridger.bridge(api_key)
    if is_zklight_bridge == -2:
        is_zklight_bridge = ["❌ Не хватает газа", ""]
    elif is_zklight_bridge == -3:
        is_zklight_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_zklight_bridge == -4:
        is_zklight_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_zklight_bridge == -6:
        is_zklight_bridge = ["❌ Произошла ошибка", ""]

    await asyncio.sleep(6)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 1/7")

    opbnb_bridger = Bridger(private_key, 'ZkBridge on opBNB', 'bsc', 'opbnb')
    is_opbnb_bridge = opbnb_bridger.bridge(api_key)
    if is_opbnb_bridge == -2:
        is_opbnb_bridge = ["❌ Не хватает газа", ""]
    elif is_opbnb_bridge == -3:
        is_opbnb_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_opbnb_bridge == -4:
        is_opbnb_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_opbnb_bridge == -6:
        is_opbnb_bridge = ["❌ Произошла ошибка", ""]

    await asyncio.sleep(5)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 2/7")

    core_bridger = Bridger(private_key, 'Mainnet Alpha', 'core', 'polygon')
    is_core_bridge = core_bridger.bridge(api_key)
    if is_core_bridge == -2:
        is_core_bridge = ["❌ Не хватает газа", ""]
    elif is_core_bridge == -3:
        is_core_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_core_bridge == -4:
        is_core_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_core_bridge == -6:
        is_core_bridge = ["❌ Произошла ошибка", ""]

    await asyncio.sleep(6)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 3/7")

    pandra_bsc_bridger = Bridger(private_key, 'Pandra', 'bsc', 'core')
    is_pandra_bsc_bridge = pandra_bsc_bridger.bridge(api_key)
    if is_pandra_bsc_bridge == -2:
        is_pandra_bsc_bridge = ["❌ Не хватает газа", ""]
    elif is_pandra_bsc_bridge == -3:
        is_pandra_bsc_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_pandra_bsc_bridge == -4:
        is_pandra_bsc_bridge = "❌ Что-то пошло не так, попробуйте заново"
    elif is_pandra_bsc_bridge == -6:
        is_pandra_bsc_bridge = ["❌ Произошла ошибка", ""]

    await asyncio.sleep(5)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 4/7")

    pandra_polygon_bridger = Bridger(private_key, 'Pandra', 'polygon', 'bsc')
    is_pandra_pol_bridge = pandra_polygon_bridger.bridge(api_key)
    if is_pandra_pol_bridge == -2:
        is_pandra_pol_bridge = ["❌ Не хватает газа", ""]
    elif is_pandra_pol_bridge == -3:
        is_pandra_pol_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_pandra_pol_bridge == -4:
        is_pandra_pol_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_pandra_pol_bridge == -6:
        is_pandra_pol_bridge = ["❌ Произошла ошибка", ""]

    await asyncio.sleep(7)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 5/7")

    pandra_core_bridger = Bridger(private_key, 'Pandra', 'core', 'polygon')
    is_pandra_core_bridge = pandra_core_bridger.bridge(api_key)
    if is_pandra_core_bridge == -2:
        is_pandra_core_bridge = ["❌ Не хватает газа", ""]
    elif is_pandra_core_bridge == -3:
        is_pandra_core_bridge = ["❌ Не найдена nft в кошельке", ""]
    elif is_pandra_core_bridge == -4:
        is_pandra_core_bridge = ["❌ Что-то пошло не так, попробуйте заново", ""]
    elif is_pandra_core_bridge == -6:
        is_pandra_core_bridge = ["❌ Произошла ошибка", ""]

    await asyncio.sleep(3)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Бридж nft 6/7")

    pandra_celo_bridger = Bridger(private_key, 'Pandra', 'celo', 'bsc')
    is_pandra_celo_bridge = pandra_celo_bridger.bridge(api_key)
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
                         "<u> 1. Минт nft </u> \n"
                         f"  🔘 <i> Greenfield Testnet </i> {is_gr_mint} \n"
                         f"  🔘 <i> ZkLightClient </i> {is_zklight_mint} \n"
                         f"  🔘 <i> ZkBridge on opBNB </i> {is_opbnb_mint} \n"
                         f"  🔘 <i> Mainnet Alpha </i> {is_main_mint} \n"
                         f"  🔘 <i> Pandra on BSC</i> {is_pandra_bnb_mint} \n"
                         f"  🔘 <i> Pandra on Polygon</i> {is_pandra_pol_mint} \n"
                         f"  🔘 <i> Pandra on Core</i> {is_pandra_core_mint} \n"
                         f"  🔘 <i> Pandra on Celo</i> {is_pandra_celo_mint} \n\n"
                         "<u> 2. Кроссчейн nft сендер (Blockchain:Transaction Hash)</u> \n"
                         f'  🔘 <i> ZkLightClient nft </i> {is_zklight_bridge[0]}{is_zklight_bridge[1]} \n'
                         f'  🔘 <i> ZkBridge on opBNB nft </i> {is_opbnb_bridge[0]}{is_opbnb_bridge[1]} \n'
                         f'  🔘 <i> Mainnet Alpha nft </i> {is_core_bridge[0]}{is_core_bridge[1]} \n'
                         f'  🔘 <i> CodeConqueror (Pandra) nft </i> {is_pandra_bsc_bridge[0]}{is_pandra_bsc_bridge[1]}\n'
                         f'  🔘 <i> PixelProwler (Pandra) nft </i> {is_pandra_pol_bridge[0]}{is_pandra_pol_bridge[1]} \n' 
                         f'  🔘 <i> MelodyMaven (Pandra) nft </i> {is_pandra_core_bridge[0]}{is_pandra_core_bridge[1]}\n'
                         f'  🔘 <i> EcoGuardian (Pandra) nft </i> {is_pandra_celo_bridge[0]}{is_pandra_celo_bridge[1]}\n\n'
                         '<u> 3. Отправка сообщений (zkMessenger): </u> \n'
                         f'  🔘 <i> из BSC в Polygon </i> {is_sending} \n\n',
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=reply_markup)
