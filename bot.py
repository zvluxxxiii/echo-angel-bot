import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode

API_TOKEN = "7307810781:AAFUOkaJr1YfbYrMVa6J6wV6xUuesG1zDF8"
GROUP_ID = -1002294772560

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

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

# Команда старт — приветствие
@dp.message(F.text == "/start", F.chat.type == "private")
async def send_welcome(message: Message):
    await message.answer(WELCOME_TEXT)

# Сообщение от пользователя — бот отправляет в группу
@dp.message(F.chat.type == "private")
async def forward_to_group(message: Message):
    username = message.from_user.username or "без ника"
    user_id = message.from_user.id
    forwarded = await bot.send_message(
        chat_id=GROUP_ID,
        text=(
            f"<b>✉️ Новое сообщение от @{username} (ID: <code>{user_id}</code>):</b>\n\n"
            f"<i>{message.text}</i>"
        ),
        reply_markup=None
    )
    # Сохраняем user_id как reply_to_message для ответа из группы
    forwarded.message_thread_id = user_id

# Ответ админа из группы — бот отправляет пользователю
@dp.message(F.chat.id == GROUP_ID, F.reply_to_message)
async def reply_to_user(message: Message):
    try:
        # Получаем ID пользователя из текста сообщения, на которое отвечают
        reply_text = message.reply_to_message.text
        if "ID:" in reply_text:
            user_id = int(reply_text.split("ID: <code>")[1].split("</code>")[0])
            await bot.send_message(chat_id=user_id, text=message.text)
    except Exception as e:
        print(f"Ошибка пересылки: {e}")
