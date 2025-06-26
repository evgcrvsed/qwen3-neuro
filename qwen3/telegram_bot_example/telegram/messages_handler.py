import asyncio
import os
import re
import time
from string import punctuation

from aiogram import Bot, Router, types, F
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram.filters import Command

from telegram_aiogram_example import bot
from qwen.qwen import QwenBot
qwen_bot = QwenBot()

router = Router()

@router.message()
async def message_handler(message: types.Message):
    print(message.chat.id)

    print(message.text)

    await bot.send_message(message.chat.id, qwen_bot.get_answer(message.chat.id, message.text))
