
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F
import asyncio
import logging

TOKEN = "7307810781:AAFUOkaJr1YfbYrMVa6J6wV6xUuesG1zDF8"
GROUP_ID = -1002294772560

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

user_cache = {}

@dp.message(F.chat.type == "private")
async def forward_to_admins(message: Message):
    fwd = await bot.send_message(
        GROUP_ID,
        f"✉️ Сообщение от @{message.from_user.username or 'без ника'} (ID: {message.from_user.id}):
{message.text}"
    )
    user_cache[fwd.message_id] = message.from_user.id

@dp.message(F.chat.id == GROUP_ID)
async def reply_from_admins(message: Message):
    if message.reply_to_message:
        original_id = message.reply_to_message.message_id
        if original_id in user_cache:
            user_id = user_cache[original_id]
            await bot.send_message(user_id, f"⋆｡°✩
{message.text}")

@dp.message(F.text == "/start")
async def start_message(message: Message):
    await message.answer("""⋆｡°✩₊
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
укажи хештег в конце сообщения —
например: #мики""")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
