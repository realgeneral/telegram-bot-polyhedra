from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("💰 Заминтить всё")
b2 = KeyboardButton("🔘 Greenfield Testnet (на BNB)")
b3 = KeyboardButton("🔘 ZkLightClient (на BNB)")
b4 = KeyboardButton("🔘 ZkBridge on opBNB (на BNB)")
b5 = KeyboardButton("🔘 Mainnet Alpha (на Core)")
b6 = KeyboardButton("🔘 Pandra (на BNB)")
b7 = KeyboardButton("🔘 Pandra (на Polygon)")
b8 = KeyboardButton("🔘 Pandra (на CORE)")
b9 = KeyboardButton("🔘 Pandra (на CELO)")
b10 = KeyboardButton("⬅ Вернуться в меню")

buttons = ReplyKeyboardMarkup(resize_keyboard=True)
buttons.row(b1).row(b2, b3).row(b4, b5).row(b6, b7).row(b8, b9).row(b10)