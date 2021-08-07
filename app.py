import callbacks
import handlers
import logging

from loader import dp
from aiogram import executor
from utils.db_api.database import create_db


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


async def on_startup(dp):
    await create_db()
    logging.info(
        msg="Бот запущен без ошибок.")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
