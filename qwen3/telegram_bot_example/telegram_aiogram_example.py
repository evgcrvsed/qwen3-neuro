# pip install aiogram

import logging, time, asyncio, os
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
import config

# Инициализируем бота
bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Подключаем роуты
from telegram import start, messages_handler

async def main_bot():
    dp.include_routers(
        start.router,
        messages_handler.router
    )

    await bot.delete_my_commands()
    basic_commands = [
        BotCommand(command="/start", description="Начать")
    ]
    await bot.set_my_commands(commands=basic_commands)

    await dp.start_polling(bot, skip_updates=True)


async def main():
    await asyncio.gather(main_bot())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
