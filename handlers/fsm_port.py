from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import bot, DESTINATION_DIR
from database.sql_commands import Database
from aiogram.dispatcher import FSMContext


class FromStates(StatesGroup):
    nickname = State()
    bio = State()
    photo = State()

async def fsm_form(message: types.Message):
    await message.answer("Добро пожаловать!")
    await message.answer("Как вас зовут?")
    await FromStates.nickname.set()

async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FromStates.next()
    await bot.send_message(chat_id=message.chat.id,
                           text="Расскажите о себе")

async def process_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["bio"] = message.text
    await FromStates.next()
    await bot.send_message(chat_id=message.chat.id,
                           text="Отправьте ваше фото")

async def process_photo(message: types.Message, state: FSMContext):
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=DESTINATION_DIR
    )
    async with state.proxy() as data:
        data["photo"] = path.name
    with open(path.name, "rb") as photo:
        await bot.send_photo(chat_id=message.chat.id,
                             photo=photo,
                             caption=f"Проверьте введённые данные\n"
                                    f"Имя: {data['name']}\n"
                                    f"Bio: {data['bio']}\n")
    await state.finish()

def register_fsm_handlers(dp: Dispatcher):
    dp.register_message_handler(fsm_form, commands=['fsm_start'])
    dp.register_message_handler(process_name, state=FromStates.nickname,
                                    content_types=['text'])
    dp.register_message_handler(process_bio, state=FromStates.bio,
                                    content_types=['text'])
    dp.register_message_handler(process_photo, state=FromStates.photo,
                                    content_types=types.ContentTypes.PHOTO)