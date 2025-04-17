import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode

API_TOKEN = "7307810781:AAFUOkaJr1YfbYrMVa6J6wV6xUuesG1zDF8"
GROUP_ID = -1002294772560

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Приветствие
WELCOME_TEXT = """
/⌒ - ⌒⌒

Привет. Это <b>эхо с небес</b>.
Если тебе тяжело — напиши.
Мы не судим, не исправляем, не уничтожаем.
Мы просто рядом.

☆ ꒰❛‿˂̵✧ ꒱

Ты не один.
Ты не одна.
И это место — для тебя.

☁️☁️☁️

Ответ может прийти не сразу,
но тебя обязательно услышат.

Чтобы написать конкретному админу,
укажи хештег в конце сообщения —
например: #ник
"""

# Обработка сообщений из лички
@dp.message(F.chat.type == "private")
async def handle_private_message(message: Message):
    username = message.from_user.username or "без ника"
    user_id = message.from_user.id
    text = message.text or "(без текста)"
    
    # Отправка в группу
    formatted = (
        f"✉️ Сообщение от @{username} (ID: <code>{user_id}</code>):\n\n"
        f"<i>{text}</i>"
    )
    await bot.send_message(chat_id=GROUP_ID, text=formatted)

    # Приветствие пользователю
    await message.answer(WELCOME_TEXT)

# Обработка сообщений из группы
@dp.message(F.chat.id == GROUP_ID)
async def handle_group_message(message: Message):
    if message.reply_to_message:
        await message.reply("Бот получил это сообщение!")
    else:
        pass

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
