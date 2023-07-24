from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("💰 Забриджить всё")
b2 = KeyboardButton("🔘 ZkLightClient (BSC->opBNB)")
b3 = KeyboardButton("🔘 ZkBridge on opBNB (BSC->opBNB)")
b4 = KeyboardButton("🔘 Mainnet Alpha (Core->Polygon)")
b5 = KeyboardButton("🔘 CodeConqueror (BSC->Core)")
b6 = KeyboardButton("🔘 PixelProwler (Polygon->BSC)")
b7 = KeyboardButton("🔘 MelodyMaven (Core->Polygon)")
b8 = KeyboardButton("🔘 EcoGuardian (Celo->BSC)")
b10 = KeyboardButton("⬅ Вернуться в меню")

bridge_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
bridge_buttons.row(b1).row(b2, b3).row(b4, b5).row(b6, b7).row(b8).row(b10)

