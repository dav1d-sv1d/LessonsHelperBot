from utils.db_api.database import db, User
import asyncio


""""""""""""""""""""""""""""""""
"""ADD NEW USER TO DATABASE"""
""""""""""""""""""""""""""""""""


async def add_user(user_id, full_name, date, year, current_month, current_year):

    old_user = await User.query.where(User.user_id == user_id).gino.first()
    if old_user:
        return old_user
    else:
        new_user = User()
        new_user.user_id = user_id
        new_user.full_name = full_name
        new_user.month = date
        new_user.year = year
        new_user.current_month = current_month
        new_user.current_year = current_year

        await new_user.create()
        return new_user


""""""""""""""""""""""""""""""""
"""ADD LANGUAGE"""
""""""""""""""""""""""""""""""""


async def add_language(user_id, language):

    user = await User.query.where(User.user_id == user_id).gino.first()

    await user.update(language=language).apply()


""""""""""""""""""""""""""""""""
"""ADD LANGUAGE"""
""""""""""""""""""""""""""""""""


async def add_recording_time(user_id, day):

    user = await User.query.where(User.user_id == user_id).gino.first()

    month = await User.select('month').where(User.user_id == user_id).gino.first()
    year = await User.select('year').where(User.user_id == user_id).gino.first()

    await user.update(recording_time=f'{day}-{month[0]}-{year[0]}').apply()


""""""""""""""""""""""""""""""""
"""ADD TIME"""
""""""""""""""""""""""""""""""""


async def add_time(user_id, time):

    user = await User.query.where(User.user_id == user_id).gino.first()

    await user.update(recording_time=time).apply()


""""""""""""""""""""""""""""""""
"""SELECT MONTH"""
""""""""""""""""""""""""""""""""


async def get_month(user_id):

    month = await User.select('month').where(User.user_id == user_id).gino.first()

    return month[0]


""""""""""""""""""""""""""""""""
"""SELECT YEAR"""
""""""""""""""""""""""""""""""""


async def get_year(user_id):

    year = await User.select('year').where(User.user_id == user_id).gino.first()

    return year[0]


""""""""""""""""""""""""""""""""
"""SELECT CURRENT DATE"""
""""""""""""""""""""""""""""""""


async def get_current_date(user_id):

    year = await User.select('current_year').where(User.user_id == user_id).gino.first()
    month = await User.select('current_month').where(User.user_id == user_id).gino.first()

    return [year[0], month[0]]


""""""""""""""""""""""""""""""""
"""UPDATE MONTH"""
""""""""""""""""""""""""""""""""


async def update_month_plus(user_id):

    user = await User.query.where(User.user_id == user_id).gino.first()

    month = await User.select('month').where(User.user_id == user.user_id).gino.first()

    month_ = month[0]
    month_ += 1

    await user.update(month=int(month_)).apply()


""""""""""""""""""""""""""""""""
"""UPDATE MONTH"""
""""""""""""""""""""""""""""""""


async def update_month_minus(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()

    month = await User.select('month').where(User.user_id == user.user_id).gino.first()

    month_ = month[0]
    month_ -= 1

    await user.update(month=month_).apply()


""""""""""""""""""""""""""""""""
"""UPDATE MONTH"""
""""""""""""""""""""""""""""""""


async def update_month(user_id, num):
    user = await User.query.where(User.user_id == user_id).gino.first()

    await user.update(month=num).apply()


""""""""""""""""""""""""""""""""
"""UPDATE MONTH"""
""""""""""""""""""""""""""""""""


async def update_year(user_id, num):

    user = await User.query.where(User.user_id == user_id).gino.first()

    await user.update(year=num).apply()


""""""""""""""""""""""""""""""""
"""UPDATE YEAR"""
""""""""""""""""""""""""""""""""


async def update_year_plus(user_id):

    user = await User.query.where(User.user_id == user_id).gino.first()

    year = await User.select('year').where(User.user_id == user.user_id).gino.first()

    year_ = year[0]
    year_ += 1

    await user.update(year=int(year_)).apply()


""""""""""""""""""""""""""""""""
"""UPDATE YEAR"""
""""""""""""""""""""""""""""""""


async def update_year_minus(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()

    year = await User.select('year').where(User.user_id == user.user_id).gino.first()

    year_ = year[0]
    year_ -= 1

    await user.update(year=year_).apply()
