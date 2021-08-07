from loader import dp, bot, types


@dp.callback_query_handler(text="None")
async def click_none(call: types.CallbackQuery):
    await call.answer()
