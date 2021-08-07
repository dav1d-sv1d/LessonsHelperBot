from loader import dp, bot, types
from aiogram.dispatcher.filters import CommandStart
from keyboards.inline.inline import send_calendar, select_language
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import calendar
import datetime
from utils.db_api.commands import add_user


@dp.message_handler(CommandStart())
async def send_choice_language(message: types.Message):

    await add_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        date=datetime.datetime.now().month,
        year=datetime.datetime.now().year,
        current_year=datetime.datetime.now().year,
        current_month=datetime.datetime.now().month
    )

    await message.answer(text="Выберите, на какой язык хотите сделать бронь.", reply_markup=select_language())

