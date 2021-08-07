from loader import dp, bot, types
from keyboards.inline.inline import sign_for_lesson
from utils.db_api.commands import add_recording_time


@dp.callback_query_handler(text=["01", "02", "03", "04", "05",
                                 "06", "07", "08", "09", "10",
                                 "11", "12", "13", "14", "15",
                                 "16", "17", "18", "19", "20",
                                 "21", "22", "23", "24", "25",
                                 "26", "27", "28", "29", "30",
                                 "31"])
async def select_time(call: types.CallbackQuery):

    await add_recording_time(
        user_id=call.from_user.id,
        day=call.data
    )

    await call.message.edit_text(text="Запишитесь на пробное занятие.", reply_markup=sign_for_lesson())
