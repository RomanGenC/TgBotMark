from aiogram import Router, F
from aiogram.types import Message
# import DevTelegramBot
from aiogram.enums.dice_emoji import DiceEmoji

router = Router()


@router.message(F.text == "/help")  # Все функции
async def help_command(message: Message):
    await message.answer(f"/start\n/giveme5\n/help\nПомогите снять замеры\nКраткая теория\n/play\n/kazino")


@router.message(F.text == "Помогите снять замеры")  # Ответ на замеры
async def help_mem(message: Message):
    await message.answer("Пиздуй сам замеры снимай")


@router.message(F.text == "Краткая теория")  # Ответ на краткую теорию
async def help_teor(message: Message):
    await message.answer(f"У тебя штангенциркуль маленький ха-ха")


@router.message(F.text == "/giveme5")  # 5 раз клоун
async def five_clown(message: Message):
    for i in range(5):
        await message.answer("Clown")


@router.message(F.text == "/play")  # мини-игры телеграм
async def play(message: Message):
    await message.answer_dice(DiceEmoji.DICE)
    await message.answer_dice(DiceEmoji.BOWLING)
    await message.answer_dice(DiceEmoji.BASKETBALL)
    await message.answer_dice(DiceEmoji.DART)
    await message.answer_dice(DiceEmoji.FOOTBALL)


@router.message(F.text == "/kazino")  # казино
async def kazino(message: Message):
    await message.answer_dice(DiceEmoji.SLOT_MACHINE)


@router.message()  # скачивает рилс и ответ на смс не по команде
async def button(message: Message):  # скачать видео с instagram и дефолт ответ
    if 'www.' in message.text:
        source = message.text
        source = source.replace('www.', 'dd')
        await message.answer(source)
    # else:
    #     await message.answer("Пиши нормальные команды попуск")
    #     await message.answer("Я не уважаю карена, он плохо считает лабы")
    # await message.reply(message.text)

# @router.message(F.text.lower() == "/maks")  # отправить смс в другой чат
# async def spec_button(message: Message):
#     await DevTelegramBot.bot.send_message(chat_id=402622913, text="Ну что")
