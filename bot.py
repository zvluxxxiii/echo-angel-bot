import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

# Токен и ID твоей группы
TOKEN = "7307810781:AAFUOkaJr1YfbYrMVa6J6wV6xUuesG1zDF8"
GROUP_ID = -1002294772560

# Инициализация
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Приветствие по /start
@dp.message(CommandStart())
async def handle_start(message: Message):
    await message.answer(
        "<b>⋆｡°✩₊</b>\n"
        "/ᐠ – ˕ –マ\n\n"
        "<b>Привет. Это “Эхо с небес”.</b>\n"
        "Если тебе тяжело — напиши.\n"
        "Мы не судим, не исправляем, не умничаем.\n"
        "Мы просто рядом.\n\n"
        "✩ ꒰՞•ﻌ•՞꒱\n"
        "Ты не один.\n"
        "Ты не одна.\n"
        "И это место — для тебя.\n\n"
        "⭒ﾟ･｡☆･｡\n"
        "Ответ может прийти не сразу,\n"
        "но тебя обязательно услышат.\n\n"
        "Чтобы написать конкретному админу,\n"
        "укажи хештег в конце сообщения — например: #мики"
    )

# Пересылка сообщений в группу
@dp.message(F.chat.type == "private", F.text)
async def forward_to_group(message: Message):
    text = (
        f"✉️ Сообщение от @{message.from_user.username or 'без ника'} "
        f"(ID: <code>{message.from_user.id}</code>):\n\n"
        f"{message.text}"
    )
    await bot.send_message(GROUP_ID, text)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
