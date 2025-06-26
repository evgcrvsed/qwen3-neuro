import os, time
from typing import Union
from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, BotCommand
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.input_file import FSInputFile
from aiogram.enums import ParseMode

from telegram_aiogram_example import bot
import config

router = Router()

@router.callback_query(F.data == 'start')
@router.message(Command("start"))
async def start(clb: Union[Message, CallbackQuery]) -> None:
    chat_id = clb.chat.id if isinstance(clb, Message) else clb.message.chat.id

    await bot.send_message(
        chat_id=chat_id,
        text='Введите ваш запрос:'
    )
