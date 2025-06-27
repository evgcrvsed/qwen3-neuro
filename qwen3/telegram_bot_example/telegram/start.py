from typing import Union
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from telegram_aiogram_example import bot

router = Router()

@router.message(Command("start"))
async def start_handler(clb: Union[Message]) -> None:
    chat_id = clb.chat.id if isinstance(clb, Message) else clb.message.chat.id

    await bot.send_message(
        chat_id=chat_id,
        text='Введите ваш запрос:'
    )
    await bot.delete_message(chat_id=chat_id, message_id=clb.message_id)