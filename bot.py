import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Головне меню з чотирма кнопками
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Калькулятор судового збору")],
        [KeyboardButton(text="Чекліст документів")],
        [KeyboardButton(text="Генерація документів")],
        [KeyboardButton(text="Викликати адвоката")],
    ],
    resize_keyboard=True,
)


# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "Вітаю! Я юридичний бот-помічник.\n\n"
        "Я допоможу Вам:\n"
        "— розрахувати судовий збір за Вашим зверненням;\n"
        "— дізнатися, які документи потрібно подати до суду;\n"
        "— згенерувати готовий документ за шаблоном;\n"
        "— звʼязатися з адвокатом для консультації.\n\n"
        "Оберіть, що Вас цікавить:"
    )
    await message.answer(text, reply_markup=main_menu)


# Обробники кнопок головного меню (поки що заглушки)
@dp.message(F.text == "Калькулятор судового збору")
async def calculator_handler(message: Message):
    await message.answer("Модуль «Калькулятор судового збору» ще в розробці.")


@dp.message(F.text == "Чекліст документів")
async def checklist_handler(message: Message):
    await message.answer("Модуль «Чекліст документів» ще в розробці.")


@dp.message(F.text == "Генерація документів")
async def generation_handler(message: Message):
    await message.answer("Модуль «Генерація документів» ще в розробці.")


@dp.message(F.text == "Викликати адвоката")
async def lawyer_handler(message: Message):
    await message.answer("Модуль «Викликати адвоката» ще в розробці.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())