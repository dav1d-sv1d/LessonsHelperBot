from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

""""""""""""""""""""""""""""""
"""OCTOBER"""
""""""""""""""""""""""""""""""

october = [
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " ", " "]],

        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["01", "02", "03"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["04", "05", "06", "07", "08", "09", "10"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["11", "12", "13", "14", "15", "16", "17"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["18", "19", "20", "21", "22", "23", "24"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["25", "26", "27", "28", "29", "30", "31"]]

    ]
]

