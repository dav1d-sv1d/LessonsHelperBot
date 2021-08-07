from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from googleapiclient.discovery import build
from datetime import datetime
from google.oauth2 import service_account
import calendar
from utils.db_api.commands import get_month, get_year, get_current_date
from .months_keyboards.januari import januari
from .months_keyboards.february import february
from .months_keyboards.march import march
from .months_keyboards.april import april
from .months_keyboards.may import may
from .months_keyboards.june import june
from .months_keyboards.july import july
from .months_keyboards.august import august
from .months_keyboards.september import september
from .months_keyboards.october import october
from .months_keyboards.november import november
from .months_keyboards.december import december


""""""""""""""""""""""""""""""""""""""
"""SELECT LANGUAGE LESSON"""
""""""""""""""""""""""""""""""""""""""


def select_language():
    language = service_account.Credentials.from_service_account_file(
        'keys.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    service = build(
        'sheets',
        'v4',
        credentials=language
    )

    sheet = service.spreadsheets()

    result = sheet.values().get(
        spreadsheetId='1-BMpuUlhSv_QLcvRGIRxhj491hlmgNmIbxYWo2dZS5I',
        range="Преподаватели!B3:B"
    ).execute()

    keyboard = InlineKeyboardMarkup(row_width=2)
    for item in result["values"]:
        if item:
            keyboard.insert(
                InlineKeyboardButton(
                    text=item[0].strip(),
                    callback_data=item[0].strip()
                )
            )

    return keyboard


""""""""""""""""""""""""""""""""""""""
"""SELECT TIME"""
""""""""""""""""""""""""""""""""""""""


def select_time():

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text="Время 🕘",
                callback_data="Time"
            ),

        ],
        [
            InlineKeyboardButton(
                text=" ",
                callback_data="None"
            )
        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data="None"
            ) for item in [" ", " "]],

            *[InlineKeyboardButton(
                text=item,
                callback_data=item
            ) for item in ["8:00", "8:30", "9:00"]]

        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data=item
            ) for item in ["9:30", "10:00", "10:30", "11:00"]]
        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data=item
            ) for item in ["11:30", "12:00", "12:30", "13:00"]]
        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data=item
            ) for item in ["13:30", "14:00", "14:30", "15:00"]]
        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data=item
            ) for item in ["15:30", "16:00", "16:30", "17:00"]]
        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data=item
            ) for item in ["17:30", "18:00", "18:30", "19:00"]]
        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data=item
            ) for item in ["19:30", "20:00", "20:30", "21:00"]]
        ],
        [
            InlineKeyboardButton(
                text="21:30",
                callback_data="21:30"
            ),

            *[InlineKeyboardButton(
                text=item,
                callback_data="None"
            ) for item in [" ", " ", " "]]
        ],

        [
            InlineKeyboardButton(
                text=" ",
                callback_data="None"
            )
        ],

    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    return keyboard


""""""""""""""""""""""""""""""""""""""
"""SIGN FOR LESSON"""
""""""""""""""""""""""""""""""""""""""


def sign_for_lesson():
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text="Записаться на пробное занятие",
                callback_data="Sign for lesson"
            )
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard


async def send_calendar(user_id):

    mth = await get_month(
        user_id=user_id
    )

    year = await get_year(
        user_id=user_id
    )

    current_date = await get_current_date(
        user_id=user_id
    )

    months = {
        1: ["Январь ☃", januari],
        2: ["Февраль ❄", february],
        3: ["Март 🌱", march],
        4: ["Апрель 🌸", april],
        5: ["Май 🧺", may],
        6: ["Июнь 🦋", june],
        7: ["Июль 🏝", july],
        8: ["Август ⛱", august],
        9: ["Сентябрь 🥀", september],
        10: ["Октябрь 🥢", october],
        11: ["Ноябрь 🌧", november],
        12: ["Декабрь 🎄", december]

    }

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=f"{months[mth][0]} {year}",
                callback_data="None"
            )
        ],
        [
            *[InlineKeyboardButton(
                text=item,
                callback_data="None"
            ) for item in ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]]
        ],
        *months[mth][1],
        [

            InlineKeyboardButton(
                text=" ",
                callback_data="None"
            ) if mth == current_date[1] and current_date[0] == year else InlineKeyboardButton(
                text="◀",
                callback_data="◀"
            ),

            InlineKeyboardButton(
                text=str(months[mth][0][:-1]),
                callback_data="None"
            ),

            InlineKeyboardButton(
                text="▶",
                callback_data="▶"
            ) if year != 9999 else InlineKeyboardButton(
                text=" ",
                callback_data="None"
            )

        ],
        [
            InlineKeyboardButton(
                text=" ",
                callback_data="None"
            ) if mth == current_date[1] and current_date[0] == year else InlineKeyboardButton(
                text="⏮ К текущему",
                callback_data="to the start"
            ),

        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard
