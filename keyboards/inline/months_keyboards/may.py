from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

""""""""""""""""""""""""""""""
"""MAY"""
""""""""""""""""""""""""""""""

may = [
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " ", " ", " ", " "]],

        InlineKeyboardButton(
            text="01",
            callback_data="01"
        )

    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["02", "03", "04", "05", "06", "07", "08"]]
    ],
    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["09", "10", "11", "12", "13", "14", "15"]]
    ],

    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["16", "17", "18", "19", "20", "21", "22"]]
    ],

    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["23", "24", "25", "26", "27", "28", "29"]]
    ],

    [
        *[InlineKeyboardButton(
            text=item,
            callback_data=item
        ) for item in ["30", "31"]],


        *[InlineKeyboardButton(
            text=item,
            callback_data="None"
        ) for item in [" ", " ", " ", " ", " "]]

    ]
]
