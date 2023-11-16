from aiogram import Router, F
from aiogram.types import Message
import random
import MyKeyboard

router = Router()
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


# Работа с обработкой сообщений
@router.message(F.text == "/start")  # Приветствие
async def start(message: Message):
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
