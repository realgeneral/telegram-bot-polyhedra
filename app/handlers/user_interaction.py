from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states import UserFollowing


@dp.message_handler(commands=['restart'], state='*')
async def restart_cmd(message: types.Message):
    await start_cmd(message)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    buttons = [
        KeyboardButton(text="🚀 Начать"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)

    await UserFollowing.start_navigation.set()
    await message.answer("Приветствую вас в <b>Polyhedra Automatization</b> ! 🤖👋 \n\n"
                         "📍 Рекомендую ознакомиться с <a href='https://t.me/trioinweb3/13'>гайдом</a> 📍\n\n"
                         "Бот выполняент:\n"
                         "<u> 1. Минт nft: </u> \n"
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
                         '<u>Необходимое количество токенов для оплаты газа </u> \n'
                         ' BNB = <i>0.02065</i> \n'
                         ' Matic = <i>3.1</i> \n'
                         ' Core = <i>2.5</i> \n'
                         ' Celo = <i>5</i>',
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=reply_markup)


@dp.message_handler(Text(equals="🚀 Начать"), state=UserFollowing.start_navigation)
async def request_private_key(message: types.Message):
    await UserFollowing.send_API.set()
    await message.answer("👝 *Отправьте свой private key* \n\n"
                         "_Бот не собирает и не хранит ваши личные данные или ключи. "
                         "Проект является полностью открытым и прозрачным, и его исходный код (Open Source) доступен "
                         "для всех. \n "
                         "GitHub: https://github.com/realgeneral/telegram-bot-polyhedra_",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=UserFollowing.send_API)
async def request_API(message: types.Message, state: FSMContext):
    wait_message = await message.answer("⏳ Получаю private key...", reply_markup=ReplyKeyboardRemove())
    private_key = message.text.strip()
    await state.update_data(private_key=private_key)
    await bot.delete_message(chat_id=wait_message.chat.id,
                             message_id=wait_message.message_id)
    await UserFollowing.get_api_keys.set()
    await message.answer("👝 <b>Предоставьте API key от moralis</b> \n\n"
                         "<i><a href='https://docs.moralis.io/web3-data-api/evm/get-your-api-key'>Здесь</a> "
                         "туториал как получить ключ</i>",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=UserFollowing.get_api_keys)
async def private_keys(message: types.Message, state: FSMContext):
    api_key = message.text.strip()
    await state.update_data(api_key=api_key)

    buttons = [
        KeyboardButton(text="⬅ Вернуться в меню"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons],
                                       resize_keyboard=True)

    await UserFollowing.wallet_menu.set()
    await message.answer("😌 *Ключи успешно записаны*",
                         parse_mode=types.ParseMode.MARKDOWN,
                         reply_markup=reply_markup)



