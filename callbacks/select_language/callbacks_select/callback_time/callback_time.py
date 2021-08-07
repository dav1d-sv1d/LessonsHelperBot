from loader import dp, bot, types


@dp.callback_query_handler(text="Time")
async def click_time(call: types.CallbackQuery):
    await call.answer()
