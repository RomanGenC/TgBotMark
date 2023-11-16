from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, KeyboardButtonPollType, InlineKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Спец. кнопки'),
            KeyboardButton(text='Ссылки'),
        ],
        [
            KeyboardButton(text='Скачать reels'),
            KeyboardButton(text='Половодов'),
        ],
        [
            KeyboardButton(text='Узнать ID'),
            KeyboardButton(text='Цитата')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписаться", url="https://t.me/formemas")
        ]
    ]
)

links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="VK", url="https://vk.com/tdm_bot1"),
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=RomanKadykov")
        ]
    ]
)
spec_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить гео", request_location=True),
            KeyboardButton(text="Отправить контакт", request_contact=True),
            KeyboardButton(text="Создать Викторину", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)

