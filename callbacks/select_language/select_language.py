from loader import dp, bot, types
from googleapiclient.discovery import build
from google.oauth2 import service_account
from keyboards.inline.inline import select_time
from utils.db_api.commands import add_language


credentials = service_account.Credentials.from_service_account_file(
    'keys.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)


service = build(
    'sheets',
    'v4',
    credentials=credentials
)

sheet = service.spreadsheets()

result = sheet.values().get(
    spreadsheetId='1-BMpuUlhSv_QLcvRGIRxhj491hlmgNmIbxYWo2dZS5I',
    range="Преподаватели!B3:B"
).execute()


list = [Item[0].strip() for Item in result["values"] if Item]


@dp.callback_query_handler(text=list)
async def Callbacks(call: types.CallbackQuery):
    if call.data:

        await add_language(
            user_id=call.from_user.id,
            language=call.data[:-3]
        )

        await call.message.edit_text(text="Выберите время.", reply_markup=select_time())


