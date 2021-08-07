from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

""""""""""""""""""""""""""""""
"""SEPTEMBER"""
""""""""""""""""""""""""""""""

september = [
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " "]],

        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["01", "02", "03", "04", "05"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["06", "07", "08", "09", "10", "11", "12"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["13", "14", "15", "16", "17", "18", "19"]]
    ],

    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["20", "21", "22", "23", "24", "25", "26"]]
    ],

    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["27", "28", "29", "30"]],

        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " "]],

    ]

]
