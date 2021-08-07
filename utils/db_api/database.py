from gino import Gino
from sqlalchemy import (Column, Integer, BigInteger, Sequence,
                        String, TIMESTAMP, Boolean, JSON, DateTime)

from sqlalchemy import sql
from sqlalchemy.sql import text
from gino.schema import GinoSchemaVisitor

from aiogram.types import InlineKeyboardMarkup

from data.config import DB_PASS, DB_USER, host
import json
from datetime import datetime
import psycopg2


db = Gino()


class User(db.Model):
    __tablename__ = "lessons"
    query: sql.Select
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    recording_time = Column(String(20))
    teacher = Column(String())
    language = Column(String(20))
    month = Column(Integer())
    year = Column(Integer())
    current_month = Column(Integer())
    current_year = Column(Integer())




async def create_db():
    # Устанавливаем связь с базой данных
    await db.set_bind(f'postgresql://{DB_USER}:{DB_PASS}@{host}/gino')
    db.gino: GinoSchemaVisitor

    # Создаем таблицы
    await db.gino.create_all()
