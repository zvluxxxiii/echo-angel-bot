import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode

API_TOKEN = "7307810781:AAFUOkaJr1YfbYrMVa6J6wV6xUuesG1zDF8"
GROUP_ID = -1002294772560

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Кэш связи: ID сообщения в группе → ID пользователя
message_links = {}

WELCOME_TEXT = """
⋆｡°✩₊
/ᐠ – ˕ –マ

Привет. Это “Эхо с небес”.
Если тебе тяжело — напиши.
Мы не судим, не исправляем, не умничаем.
Мы просто рядом.

✩ ꒰՞•ﻌ•՞꒱
Ты не один.
Ты не одна.
И это место — для тебя.

⭒ﾟ･｡☆･｡
Ответ может прийти не сразу,
но тебя обязательно услышат.

Чтобы написать конкретному админу,
укажи хештег в конце сообщения — например: #мики
"""

# Приветствие на /start
@dp.message(F.text == "/start", F.chat.type == "private")
async def send_welcome(message: Message):
    await message.answer(WELCOME_TEXT)

# Пересылка сообщений из ЛС в группу
@dp.message(F.chat.type == "private", F.text)
async def handle_private(message: Message):
    username = message.from_user.username or "без ника"
    user_id = message.from_user.id
    text = message.text or "(пусто)"

    sent = await bot.send_message(
        GROUP_ID,
        f"<b>✉️ Сообщение от @{username} (ID: <code>{user_id}</code>):</b>\n\n<i>{text}</i>"
    )
    # Запоминаем ID отправителя
    message_links[sent.message_id] = user_id

# Ответы админов → пользователю
@dp.message(F.chat.id == GROUP_ID, F.reply_to_message)
async def reply_from_admin(message: Message):
    original = message.reply_to_message
    original_id = original.message_id

    if original_id in message_links:
        user_id = message_links[original_id]
        await bot.send_message(chat_id=user_id, text=message.text)
