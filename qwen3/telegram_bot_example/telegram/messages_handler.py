from aiogram import Router, types
from telegram_aiogram_example import bot
from qwen.qwen import QwenBot

qwen_bot = QwenBot()
router = Router()

@router.message()
async def message_handler(message: types.Message):
    print(message.chat.id)
    print(message.text)
    answer = qwen_bot.get_answer(message.chat.id, message.text)
    await bot.send_message(message.chat.id, answer)
