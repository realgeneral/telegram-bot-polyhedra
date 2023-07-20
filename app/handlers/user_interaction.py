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
