from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import main_kb, inline_kb
from lexicon.lexicon import LEXICON

router = Router()

# Хендлер на команду /start
@router.message(Command("start"))
async def process_start_command(message: Message):
    await message.answer(LEXICON['start'], reply_markup=main_kb)

# Хендлер на команду /help
@router.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer(LEXICON['help'])

# Хендлер на текстовые сообщения
@router.message(F.text == "Меню 1")
async def process_menu1(message: Message):
    await message.answer(LEXICON['menu1'], reply_markup=inline_kb)

@router.message(F.text == "Меню 2")
async def process_menu2(message: Message):
    await message.answer(LEXICON['menu2'])

# Хендлер на callback_query
@router.callback_query(F.data == "button1")
async def process_button1(callback: CallbackQuery):
    await callback.answer("Вы нажали кнопку 1!")

@router.callback_query(F.data == "button2")
async def process_button2(callback: CallbackQuery):
    await callback.answer("Вы нажали кнопку 2!") 