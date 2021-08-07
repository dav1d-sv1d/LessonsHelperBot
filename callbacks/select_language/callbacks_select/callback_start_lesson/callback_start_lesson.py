from loader import dp, bot, types


@dp.callback_query_handler(text="Sign for lesson")
async def lesson(call: types.CallbackQuery):
    await call.message.edit_text(text="Спасибо, ждите своего урока:)")
