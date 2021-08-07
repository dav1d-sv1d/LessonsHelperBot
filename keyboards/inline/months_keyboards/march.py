from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

""""""""""""""""""""""""""""""
"""MARCH"""
""""""""""""""""""""""""""""""

march = [
    [
        InlineKeyboardButton(
            text=" ",
            callback_data="None"
        ),

        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["01", "02", "03", "04", "05", "06"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["07", "08", "09", "10", "11", "12", "13"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["14", "15", "16", "17", "18", "19", "20"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["21", "22", "23", "24", "25", "26", "27"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["28", "29", "30", "31"]],

        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " "]]
    ]
]

