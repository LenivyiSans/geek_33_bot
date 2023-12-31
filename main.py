from aiogram.utils import executor
from config import dp
from handlers import start, callback, chat_actions, fsm_port
from database import sql_commands


async def onstart_up(_):
    db = sql_commands.Database()
    db.sql_create_tables()

start.reg_start_handler(dp)
fsm_port.register_fsm_handlers(dp)
callback.register_callback_handlers(dp)
chat_actions.register_chat_actions_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=onstart_up
    )