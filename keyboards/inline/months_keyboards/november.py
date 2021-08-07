from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

""""""""""""""""""""""""""""""
"""NOVEMBER"""
""""""""""""""""""""""""""""""

november = [
    [

        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["01", "02", "03", "04", "05", "06", "07"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["08", "09", "10", "11", "12", "13", "14"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["15", "16", "17", "18", "19", "20", "21"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["22", "23", "24", "25", "26", "27", "28"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["29", "30"]],

        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " ", " ", " "]]
    ]
]

