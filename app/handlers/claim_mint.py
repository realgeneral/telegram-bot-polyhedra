from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing
from app.utils import Minter
from app.keyboards import mint_buttons


@dp.message_handler(Text(equals="⛏ Минт nft"), state=UserFollowing.choose_point)
async def send_menu(message: types.Message, state: FSMContext):
    await UserFollowing.choose_point.set()
    await message.answer(f"Выберите действие:", parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="💰 Заминтить всё"), state=UserFollowing.choose_point)
async def claim_mint_all(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/8")

    greenfield_minter = Minter(private_key, 'bsc', 'Greenfield Testnet')
    is_gr_mint = await greenfield_minter.mint()
    if is_gr_mint == -2:
        is_gr_mint = "❌ Не хватает газа"
    elif is_gr_mint == -5:
        is_gr_mint = "❌ Claimed already"
    elif is_gr_mint == -6:
        is_gr_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/8")

    zklight_minter = Minter(private_key, 'bsc', 'ZkLightClient')
    is_zklight_mint = await zklight_minter.mint()
    if is_zklight_mint == -2:
        is_zklight_mint = "❌ Не хватает газа"
    elif is_zklight_mint == -5:
        is_zklight_mint = "❌ Claimed already"
    elif is_zklight_mint == -6:
        is_zklight_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 2/8")

    opbnb_minter = Minter(private_key, 'bsc', 'ZkBridge on opBNB')
    is_opbnb_mint = await opbnb_minter.mint()
    if is_opbnb_mint == -2:
        is_opbnb_mint = "❌ Не хватает газа"
    elif is_opbnb_mint == -5:
        is_opbnb_mint = "❌ Claimed already"
    elif is_opbnb_mint == -6:
        is_opbnb_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 3/8")

    mainnetalpha_minter = Minter(private_key, 'core', 'Mainnet Alpha')
    is_main_mint = await mainnetalpha_minter.mint()
    if is_main_mint == -2:
        is_main_mint = "❌ Не хватает газа"
    elif is_main_mint == -5:
        is_main_mint = "❌ Claimed already"
    elif is_main_mint == -6:
        is_main_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 4/8")

    pandra_bnb_minter = Minter(private_key, 'bsc', 'Pandra')
    is_pandra_bnb_mint = await pandra_bnb_minter.mint()
    if is_pandra_bnb_mint == -2:
        is_pandra_bnb_mint = "❌ Не хватает газа"
    elif is_pandra_bnb_mint == -5:
        is_pandra_bnb_mint = "❌ Claimed already"
    elif is_pandra_bnb_mint == -6:
        is_pandra_bnb_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 5/8")

    pandra_pol_minter = Minter(private_key, 'polygon', 'Pandra')
    is_pandra_pol_mint = await pandra_pol_minter.mint()
    if is_pandra_pol_mint == -2:
        is_pandra_pol_mint = "❌ Не хватает газа"
    elif is_pandra_pol_mint == -5:
        is_pandra_pol_mint = "❌ Claimed already"
    elif is_pandra_pol_mint == -6:
        is_pandra_pol_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 6/8")

    pandra_core_minter = Minter(private_key, 'core', 'Pandra')
    is_pandra_core_mint = await pandra_core_minter.mint()
    if is_pandra_core_mint == -2:
        is_pandra_core_mint = "❌ Не хватает газа"
    elif is_pandra_core_mint == -5:
        is_pandra_core_mint = "❌ Claimed already"
    elif is_pandra_core_mint == -6:
        is_pandra_core_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 7/8")

    pandra_celo_minter = Minter(private_key, 'celo', 'Pandra')
    is_pandra_celo_mint = await pandra_celo_minter.mint()
    if is_pandra_celo_mint == -2:
        is_pandra_celo_mint = "❌ Не хватает газа"
    elif is_pandra_celo_mint == -5:
        is_pandra_celo_mint = "❌ Claimed already"
    elif is_pandra_celo_mint == -6:
        is_pandra_celo_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 8/8")
    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> Greenfield Testnet </i> {is_gr_mint} \n"
                         f"  🔘 <i> ZkLightClient </i> {is_zklight_mint} \n"
                         f"  🔘 <i> ZkBridge on opBNB </i> {is_opbnb_mint} \n"
                         f"  🔘 <i> Mainnet Alpha </i> {is_main_mint} \n"
                         f"  🔘 <i> Pandra on BSC</i> {is_pandra_bnb_mint} \n"
                         f"  🔘 <i> Pandra on Polygon</i> {is_pandra_pol_mint} \n"
                         f"  🔘 <i> Pandra on Core</i> {is_pandra_core_mint} \n"
                         f"  🔘 <i> Pandra on Celo</i> {is_pandra_celo_mint} \n\n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 ZkLightClient (на BNB)"), state=UserFollowing.choose_point)
async def claim_mint_zk_light_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    zklight_minter = Minter(private_key, 'bsc', 'ZkLightClient')
    is_zklight_mint = await zklight_minter.mint()
    if is_zklight_mint == -2:
        is_zklight_mint = "❌ Не хватает газа"
    elif is_zklight_mint == -5:
        is_zklight_mint = "❌ Claimed already"
    elif is_zklight_mint == -6:
        is_zklight_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")

    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> ZkLightClient </i> {is_zklight_mint} \n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 ZkBridge on opBNB (на BNB)"), state=UserFollowing.choose_point)
async def claim_mint_op_bnb_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    opbnb_minter = Minter(private_key, 'bsc', 'ZkBridge on opBNB')
    is_opbnb_mint = await opbnb_minter.mint()
    if is_opbnb_mint == -2:
        is_opbnb_mint = "❌ Не хватает газа"
    elif is_opbnb_mint == -5:
        is_opbnb_mint = "❌ Claimed already"
    elif is_opbnb_mint == -6:
        is_opbnb_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")

    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> ZkBridge on opBNB </i> {is_opbnb_mint} \n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 Mainnet Alpha (на Core)"), state=UserFollowing.choose_point)
async def claim_mint_main_net_alpha_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    mainnetalpha_minter = Minter(private_key, 'core', 'Mainnet Alpha')
    is_main_mint = await mainnetalpha_minter.mint()
    if is_main_mint == -2:
        is_main_mint = "❌ Не хватает газа"
    elif is_main_mint == -5:
        is_main_mint = "❌ Claimed already"
    elif is_main_mint == -6:
        is_main_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")

    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)
    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> Mainnet Alpha </i> {is_main_mint} \n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 Pandra (на BNB)"), state=UserFollowing.choose_point)
async def claim_mint_pandra_bnb_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    pandra_bnb_minter = Minter(private_key, 'bsc', 'Pandra')
    is_pandra_bnb_mint = await pandra_bnb_minter.mint()
    if is_pandra_bnb_mint == -2:
        is_pandra_bnb_mint = "❌ Не хватает газа"
    elif is_pandra_bnb_mint == -5:
        is_pandra_bnb_mint = "❌ Claimed already"
    elif is_pandra_bnb_mint == -6:
        is_pandra_bnb_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")
    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> Pandra on BSC</i> {is_pandra_bnb_mint} \n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 Pandra (на Polygon)"), state=UserFollowing.choose_point)
async def claim_mint_pandra_pol_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    pandra_pol_minter = Minter(private_key, 'polygon', 'Pandra')
    is_pandra_pol_mint = await pandra_pol_minter.mint()
    if is_pandra_pol_mint == -2:
        is_pandra_pol_mint = "❌ Не хватает газа"
    elif is_pandra_pol_mint == -5:
        is_pandra_pol_mint = "❌ Claimed already"
    elif is_pandra_pol_mint == -6:
        is_pandra_pol_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")

    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> Pandra on Polygon</i> {is_pandra_pol_mint} \n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 Pandra (на CORE)"), state=UserFollowing.choose_point)
async def claim_mint_pandra_core_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    pandra_core_minter = Minter(private_key, 'core', 'Pandra')
    is_pandra_core_mint = await pandra_core_minter.mint()
    if is_pandra_core_mint == -2:
        is_pandra_core_mint = "❌ Не хватает газа"
    elif is_pandra_core_mint == -5:
        is_pandra_core_mint = "❌ Claimed already"
    elif is_pandra_core_mint == -6:
        is_pandra_core_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")
    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> Pandra on Core</i> {is_pandra_core_mint} \n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 Greenfield Testnet (на BNB)"), state=UserFollowing.choose_point)
async def claim_mint_greenfield_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    greenfield_minter = Minter(private_key, 'bsc', 'Greenfield Testnet')
    is_gr_mint = await greenfield_minter.mint()
    if is_gr_mint == -2:
        is_gr_mint = "❌ Не хватает газа"
    elif is_gr_mint == -5:
        is_gr_mint = "❌ Claimed already"
    elif is_gr_mint == -6:
        is_gr_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")

    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> Greenfield Testnet </i> {is_gr_mint} \n",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)


@dp.message_handler(Text(equals="🔘 Pandra (на CELO)"), state=UserFollowing.choose_point)
async def claim_mint_pandra_celo_minter(message: types.Message, state: FSMContext):
    wait_1_message = await message.answer("⏳ Начинаю клейм ...")

    data = await state.get_data()
    private_key = data.get("private_key")

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ Начинаю mint nft 0/1")

    pandra_celo_minter = Minter(private_key, 'celo', 'Pandra')
    is_pandra_celo_mint = await pandra_celo_minter.mint()
    if is_pandra_celo_mint == -2:
        is_pandra_celo_mint = "❌ Не хватает газа"
    elif is_pandra_celo_mint == -5:
        is_pandra_celo_mint = "❌ Claimed already"
    elif is_pandra_celo_mint == -6:
        is_pandra_celo_mint = "❌ Произошла ошибка"

    await bot.edit_message_text(chat_id=wait_1_message.chat.id,
                                message_id=wait_1_message.message_id,
                                text=f"⏳ mint nft 1/1")
    await bot.delete_message(chat_id=wait_1_message.chat.id,
                             message_id=wait_1_message.message_id)

    await message.answer("📊 <b>Статистика</b> \n\n"
                         "<u> Минт nft </u> \n"
                         f"  🔘 <i> Pandra on Celo</i> {is_pandra_celo_mint}",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=mint_buttons)
