from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing


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
async def request_wallets(message: types.Message):
    await UserFollowing.ask_wallet.set()
    await message.answer("👝 *Отправьте свой кошелек* \n\n"
                         "_Если Вы хотите отправить несколько кошельков, то разделите кошельки построчно_",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=UserFollowing.ask_wallet)
async def send_wallet_stats(message: types.Message):
    user_wallets = message.text

    wait_message = await message.answer("⏳ Получаю кошельки...", reply_markup=ReplyKeyboardRemove())

    if '\n' in user_wallets:
        lst_user_wallets = user_wallets.split('\n')
        for i in range(len(lst_user_wallets)):
            lst_user_wallets[i].strip()
            if len(lst_user_wallets[i]) != 42:
                error_message = f" Неверный формат (либо ошибка в получении кошелька #{i + 1})"

                buttons = [
                    KeyboardButton(text="Попробовать снова"),
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                                   resize_keyboard=True)

                await bot.delete_message(chat_id=wait_message.chat.id,
                                         message_id=wait_message.message_id)
                await message.answer(error_message, parse_mode=types.ParseMode.MARKDOWN,
                                     reply_markup=reply_markup)
                return
        lst_user_wallets = list(set(lst_user_wallets))
        await bot.delete_message(chat_id=wait_message.chat.id,
                                 message_id=wait_message.message_id)
        success_message = await message.answer(f" _Получено кошельков: {len(lst_user_wallets)}_",
                                               parse_mode=types.ParseMode.MARKDOWN)
    else:
        user_wallet = user_wallets.strip()

        if len(user_wallet) != 42:
            error_message = f" Неверный формат кошелька"

            buttons = [
                KeyboardButton(text="Попробовать снова"),
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                               resize_keyboard=True)

            await bot.delete_message(chat_id=wait_message.chat.id,
                                     message_id=wait_message.message_id)
            await message.answer(error_message, parse_mode=types.ParseMode.MARKDOWN,
                                 reply_markup=reply_markup)
            return
        await bot.delete_message(chat_id=wait_message.chat.id,
                                 message_id=wait_message.message_id)
        lst_user_wallets = [user_wallet]
        success_message = await message.answer(f" _Кошелек успешно получен_", parse_mode=types.ParseMode.MARKDOWN)

    wait_1_message = await message.answer("⏳ Готовлю статистику...")
    response_message = ""

