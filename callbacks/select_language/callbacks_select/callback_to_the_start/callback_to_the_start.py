from loader import dp, bot, types
from keyboards.inline.inline import send_calendar
from utils.db_api.commands import update_month_plus, get_month, update_year_plus, update_month, update_year
from datetime import datetime


@dp.callback_query_handler(text="to the start")
async def click_none(call: types.CallbackQuery):

    await update_month(user_id=call.from_user.id, num=datetime.now().month)
    await update_year(user_id=call.from_user.id, num=datetime.now().year)

    await call.message.edit_reply_markup(reply_markup=await send_calendar(user_id=call.from_user.id))
