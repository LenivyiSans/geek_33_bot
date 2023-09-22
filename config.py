from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = 1751557503
BOT_PIC = 'C:/Users/TM-PC/PycharmProjects/second_old_bot/media/bot_pic.jpeg'
ANIMATION_PIC = 'C:/Users/TM-PC/PycharmProjects/second_old_bot/media/joinblink-blink.gif'
GROUP_ID = -4076324382
DESTINATION_DIR = 'C:/Users/TM-PC/PycharmProjects/second_old_bot/media'