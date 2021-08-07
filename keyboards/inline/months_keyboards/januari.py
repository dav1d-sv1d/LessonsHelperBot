from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

""""""""""""""""""""""""""""""
"""JANUARI"""
""""""""""""""""""""""""""""""

januari = [
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " ", " ", " "]],

        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["01", "02"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["03", "04", "05", "06", "07", "08", "09"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["10", "11", "12", "13", "14", "15", "16"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["17", "18", "19", "20", "21", "22", "23"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["24", "25", "26", "27", "28", "29", "30"]]
    ],
    [
        InlineKeyboardButton(
            text="30",
            callback_data="30"
        ),
        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " ", " ", " ", " "]]

    ]
]

