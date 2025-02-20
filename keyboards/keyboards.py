from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Основная клавиатура
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню 1"), KeyboardButton(text="Меню 2")],
        [KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

# Инлайн клавиатура (пример)
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Кнопка 1", callback_data="button1")],
        [InlineKeyboardButton(text="Кнопка 2", callback_data="button2")]
    ]
) 