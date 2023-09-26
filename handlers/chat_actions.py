import datetime

from config import bot, GROUP_ID
from aiogram import types, Dispatcher


async def echo_ban(message: types.Message):
    ban_word = ['shit', 'fuck', 'bitch', 'damn', 'daun']

    if message.chat.id == GROUP_ID:
        for word in ban_word:
            if word in message.text.lower().replace(" ", ' '):
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Pshol Von!!!"
                         " or Ban!!!"
            )



def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_ban)
