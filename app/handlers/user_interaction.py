import asyncio

from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing
from app.utils import Bridger, Messager, Minter


@dp.message_handler(Text(equals=["❌ Попробовать снова"]), state='*')
async def finish_get_stat(message: types.Message, state: FSMContext):
    await state.finish()
    await UserFollowing.start_navigation.set()
    await request_wallets(message)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    buttons = [
        KeyboardButton(text="🚀 Начать"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)

    await UserFollowing.start_navigation.set()
    await message.answer("Приветствую вас в <b>Polyhedra Automatization</b> ! 🤖👋 \n\n"
                         ""
                         "Бот выполняент:\n\n"
                         ""
                         "<u> 1. Минт nft (loyalty): </u> \n"
                         "  🔘 <i> Greenfield Testnet </i> (на BNB Chain) \n"
                         "  🔘 <i> ZkLightClient </i> (на BNB Chain) \n"
                         "  🔘 <i> ZkBridge on opBNB </i> (на BNB Chain) \n"
                         "  🔘 <i> Mainnet Alpha </i> (на Core) \n"
                         "  🔘 <i> Pandra </i> (на BNB Chain, Polygon, Core, Celo) \n\n"
                         "<u> 2. Кроссчейн nft сендер (zknft): </u> \n"
                         '  🔘 <i> ZkLightClient nft </i> из BSC в opBNB \n'
                         '  🔘 <i> ZkBridge on opBNB nft </i> из BSC в opBNB \n'
                         '  🔘 <i> Mainnet Alpha nft </i> из Core в Polygon \n'
                         '  🔘 <i> CodeConqueror (Pandra) nft </i> из BSC в Core \n'
                         '  🔘 <i> PixelProwler (Pandra) nft </i> из Polygon в BSC \n'
                         '  🔘 <i> MelodyMaven (Pandra) nft </i> из Core в Polygon \n'
                         '  🔘 <i> EcoGuardian (Pandra) nft </i> из Celo в BSC \n\n'
                         '<u> 3. Отправка сообщений (zkMessenger): </u> \n'
                         '  🔘 <i> из BSC в Polygon </i> \n\n'
                         ''
                         '<i> - Чтобы сминтить в сети Core необходимо раскинуть по кошелькам немного core \n'
                         ' - Также необходим газ в opBNB </i>',
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=reply_markup)


@dp.message_handler(Text(equals="🚀 Начать"), state=UserFollowing.start_navigation)
async def request_private_key(message: types.Message):
    await UserFollowing.send_API.set()
    await message.answer("👝 *Отправьте свой private key* \n\n"
                         "_Бот не собирает Ваши ключи. Проект является полностью OpenSource \n"
                         "GitHub: _",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals="🚀 Начать"), state=UserFollowing.send_API)
async def request_API(message: types.Message, state: FSMContext):
    wait_message = await message.answer("⏳ Получаю private key...", reply_markup=ReplyKeyboardRemove())
    private_key = message.text.strip()
    await state.update_data(private_key=private_key)
    await bot.delete_message(chat_id=wait_message.chat.id,
                             message_id=wait_message.message_id)
    await UserFollowing.wallet_menu.set()
    await message.answer("👝 *Отправьте API* \n\n"
                         "_ Тутор _",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=UserFollowing.wallet_menu)
async def send_menu(message: types.Message, state: FSMContext):
    api_key = message.text.strip()
    await state.update_data(api_key=api_key)

    data = await state.get_data()
    private_key = data.get("private_key")

    b1 = KeyboardButton("💰 Заклеймить всё")
    b2 = KeyboardButton("⛏ Минт nft")
    b3 = KeyboardButton("📩 Отправка сообщения")
    b4 = KeyboardButton("💸 Кроссчейн nft сендер")
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons.row(b1, b2).row(b3, b4)

    await UserFollowing.wallet_menu.set()
    await message.answer(f"# Private key *{private_key[0:6]}...{private_key[-4:]}* \n"
                         f"# API key *{api_key[0:6]}...{api_key[-4:]}*\n\n"
                         f"Выберите действие:", parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=buttons)


@dp.message_handler(Text(equals="💰 Заклеймить всё"), state=UserFollowing.wallet_menu)
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
    elif is_pandra_celo_mint == -6:
        is_pandra_celo_mint = "❌ Произошла ошибка"

    await asyncio.sleep(5)
    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 8/8. Приступаю к ")

    buttons = [
        KeyboardButton(text="⬅ Вернуться в меню"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                       resize_keyboard=True)
    await UserFollowing.claim_all.set()
    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> 1. Минт nft </u> \n"
                         f"  🔘 <i> Greenfield Testnet </i> {is_gr_mint} \n"
                         f"  🔘 <i> ZkLightClient </i> {is_zklight_mint} \n"
                         f"  🔘 <i> ZkBridge on opBNB </i> {is_opbnb_mint} \n"
                         f"  🔘 <i> Mainnet Alpha </i> {is_main_mint} \n"
                         f"  🔘 <i> Pandra on BSC</i> {is_pandra_bnb_mint} \n\n"
                         f"  🔘 <i> Pandra on Polygon</i> {is_pandra_pol_mint} \n\n"
                         f"  🔘 <i> Pandra on Core</i> {is_pandra_core_mint} \n\n"
                         f"  🔘 <i> Pandra on Celo</i> {is_pandra_celo_mint} \n\n"
                         "<u> 2. Кроссчейн nft сендер (Blockchain:Transaction Hash)</u> \n"
                         f'  🔘 <i> ZkLightClient nft </i> {} \n'
                         f'  🔘 <i> ZkBridge on opBNB nft </i> {} \n'
                         f'  🔘 <i> Mainnet Alpha nft </i> {} \n'
                         f'  🔘 <i> CodeConqueror (Pandra) nft </i> {} \n'
                         f'  🔘 <i> PixelProwler (Pandra) nft </i> {} \n'
                         f'  🔘 <i> MelodyMaven (Pandra) nft </i> {} \n'
                         f'  🔘 <i> EcoGuardian (Pandra) nft </i> {} \n\n'
                         '<u> 3. Отправка сообщений (zkMessenger): </u> \n'
                         f'  🔘 <i> из BSC в Polygon </i> {is_sending} \n\n',
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=reply_markup)
