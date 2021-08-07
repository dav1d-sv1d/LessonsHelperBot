from loader import dp, bot, types
from keyboards.inline.inline import send_calendar
from utils.db_api.commands import update_month_minus, get_month, update_year_minus, update_month


@dp.callback_query_handler(text="◀")
async def click_none(call: types.CallbackQuery):

    if await get_month(user_id=call.from_user.id) == 1:
        await update_month(user_id=call.from_user.id, num=12)
    else:
        await update_month_minus(
            user_id=call.from_user.id)

    if await get_month(user_id=call.from_user.id) == 12:
        await update_year_minus(user_id=call.from_user.id)

    await call.message.edit_reply_markup(reply_markup=await send_calendar(user_id=call.from_user.id))
