import asyncio
from aiogram import Router, F
from aiogram.types import Message
import random
import MyKeyboard
from postSQL import connection, execute_read_query, execute_query
# from DevTelegramBot import bot
from datetime import datetime

router = Router(name=__name__)
file_ids = [
    'https://sun9-56.userapi.com/impg/yXH8LfFjQOBx3mJBiMbXXHePWaSejXRtkGRtFg/mg4amHn1uqI.jpg?size=511x509&quality=96&sign=212586ac98d0053ca555bc434d1d064a&c_uniq_tag=cmqG8IRUii474TZiwtSIHXj1oFkJPEklLxM5f7crdME&type=album',
    'https://cdn27.echosevera.ru/64809353eac9120dd845a103/6484502b61cba.jpg',
    'https://sun9-16.userapi.com/impg/2wn-o56DtFaj0pI4RDJxMxLhZ3nEymX_1seTzg/Z0qqF-fV2pg.jpg?size=538x807&quality=95&sign=f32b38af73b03b1af096390f4a6bb8b6&c_uniq_tag=PoAquXDqygGvTkZRk-BDYodjgSi1VjL1mMXWcoC-oNU&type=album'
]


@router.message(F.text.lower() == "цитата")  # Цитата
async def start(message: Message):
    r = random.randint(0, 2)
    image_from_url = file_ids[r]
    result = await message.answer_photo(
        image_from_url,
        caption="Лови топ цитату"
    )
    # file_ids.append(result.photo[-1].file_id)


# delete_comment = "DELETE FROM users WHERE tg_id = 577517612"
# execute_query(connection, delete_comment)

# Работа с обработкой сообщений
@router.message(F.text == "/start")  # Приветствие
async def start(message: Message):
    flug = 0
    connection.autocommit = True
    select_users = "SELECT tg_id FROM users"
    users_id = execute_read_query(connection, select_users)
    print(users_id)
    for i in users_id:
        if message.from_user.id in i:
            flug = 1
    if flug == 1:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Ну что ты сегодня, спишь без трусиков?")
    else:
        print(users_id)
        # users_id.append(message.from_user.id)
        insert_query = (
            f"INSERT INTO users (name, tg_id) VALUES {message.from_user.first_name, message.from_user.id}"
        )
        cursor = connection.cursor()
        cursor.execute(insert_query, users_id)
        print(message.from_user.id, message.from_user.first_name)
    await message.answer(f"Hello, {message.from_user.first_name}", reply_markup=MyKeyboard.main_keyboard)


@router.message(F.text.lower() == "ссылки")  # ссылки
async def source(message: Message):
    await message.answer("Ссылки на гениального гения(создателя бота): ", reply_markup=MyKeyboard.links_keyboard)


@router.message(F.text.lower() == "спец. кнопки")  # специальные кнопки
async def spec_button(message: Message):
    await message.answer("Спец. кнопки: ", reply_markup=MyKeyboard.spec_keyboard)


@router.message(F.text.lower() == "узнать id")  # кнопка узнать id
async def teacher(message: Message):
    await message.answer(f"Твой id: {message.from_user.id}")


@router.message(F.text.lower() == "половодов")  # половодов
async def teacher(message: Message):
    await message.answer("Зачем ты нажал на эту кнопку?\nНе боишься экзамена по физике?\n💀💀💀💀💀💀💀💀")


@router.message(F.text.lower() == "скачать reels")  # скачать рилс
async def download(message: Message):
    await message.answer("Отправь мне ссылку на reels")
